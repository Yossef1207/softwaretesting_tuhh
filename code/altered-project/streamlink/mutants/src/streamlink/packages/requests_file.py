"""
Copyright 2015 Red Hat, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import errno
import io
import locale
import os
import os.path
import stat
import sys
from io import BytesIO
from urllib.parse import unquote, urljoin, urlparse

from requests import Response, codes
from requests.adapters import BaseAdapter

from streamlink.compat import is_win32
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


class FileAdapter(BaseAdapter):
    def xǁFileAdapterǁsend__mutmut_orig(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_1(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_2(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("XXGETXX", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_3(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("get", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_4(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("Get", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_5(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "XXHEADXX"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_6(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "head"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_7(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "Head"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_8(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(None)

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_9(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = None

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_10(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(None)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_11(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 or url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_12(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(None):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_13(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith("XX:XX"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_14(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = None

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_15(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=None, netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_16(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc=None)

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_17(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_18(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", )

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_19(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="XXXX")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_20(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc or url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_21(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_22(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("XXlocalhostXX", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_23(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("LOCALHOST", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_24(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("Localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_25(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", "XX.XX", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_26(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "XX..XX", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_27(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "XX-XX"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_28(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError(None)

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_29(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("XXfile: URLs with hostname components are not permittedXX")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_30(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: urls with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_31(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("FILE: URLS WITH HOSTNAME COMPONENTS ARE NOT PERMITTED")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_32(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("File: urls with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_33(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc not in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_34(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in ("XX.XX", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_35(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", "XX..XX"):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_36(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = None
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_37(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(None, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_38(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, None) + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_39(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace("/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_40(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, ) + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_41(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(None).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_42(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "XX/XX") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_43(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") - "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_44(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "XX/XX"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_45(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = None
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_46(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = None

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_47(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=None)

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_48(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(None, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_49(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, None))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_50(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_51(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, ))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_52(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip(None)))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_53(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.rstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_54(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("XX/XX")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_55(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = None
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_56(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = None

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_57(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc != "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_58(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "XX-XX":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_59(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = None
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_60(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = None
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_61(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "XXfile://XX" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_62(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "FILE://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_63(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "File://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_64(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" - os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_65(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(None, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_66(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, None) + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_67(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace("/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_68(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, ) + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_69(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(None).replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_70(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath("XX.XX").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_71(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "XX/XX") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_72(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") - "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_73(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "XX/XX"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_74(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = None

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_75(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(None) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_76(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split(None)]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_77(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.rsplit('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_78(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('XX/XX')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_79(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts or not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_80(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_81(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[1]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_82(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(None)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_83(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(1)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_84(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(None):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_85(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep not in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_86(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(None, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_87(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, None)

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_88(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_89(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, )

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_90(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(None))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_91(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts or (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_92(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith(None) or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_93(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[1].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_94(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('XX|XX') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_95(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') and path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_96(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(None)):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_97(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[1].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_98(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith('XX:XX')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_99(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = None
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_100(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(None)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_101(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(1)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_102(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith(None):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_103(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('XX|XX'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_104(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = None

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_105(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:+1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_106(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-2]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_107(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts or not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_108(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_109(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[1]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_110(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(None)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_111(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(1)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_112(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = None

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_113(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = 'XXXX'

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_114(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = None

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_115(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive - os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_116(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep - os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_117(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive or not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_118(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_119(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(None):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_120(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = None

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_121(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep - os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_122(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(None, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_123(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(*path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_124(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, )

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_125(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = None
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_126(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(None, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_127(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, None)
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_128(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open("rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_129(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, )
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_130(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "XXrbXX")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_131(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "RB")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_132(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "Rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_133(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = None
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_134(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno != errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_135(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = None
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_136(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno != errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_137(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = None
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_138(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = None

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_139(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = None
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_140(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(None)
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_141(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(None).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_142(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(None))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_143(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(True))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_144(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = None
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_145(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(None)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_146(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = None

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_147(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['XXContent-LengthXX'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_148(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['content-length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_149(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['CONTENT-LENGTH'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_150(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_151(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = None
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_152(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = None

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_153(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = None
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_154(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(None)
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_155(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(None):
                resp.headers['Content-Length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_156(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-Length'] = None

        return resp
    def xǁFileAdapterǁsend__mutmut_157(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['XXContent-LengthXX'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_158(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['content-length'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_159(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['CONTENT-LENGTH'] = resp_stat.st_size

        return resp
    def xǁFileAdapterǁsend__mutmut_160(self, request, **kwargs):
        """ Wraps a file, described in request, in a Response object.

            :param request: The PreparedRequest` being "sent".
            :returns: a Response object containing the file
        """

        # Check that the method makes sense. Only support GET
        if request.method not in ("GET", "HEAD"):
            raise ValueError(f"Invalid request method {request.method}")

        # Parse the URL
        url_parts = urlparse(request.url)

        # Make the Windows URLs slightly nicer
        if is_win32 and url_parts.netloc.endswith(":"):
            url_parts = url_parts._replace(path=f"/{url_parts.netloc}{url_parts.path}", netloc="")

        # Reject URLs with a hostname component
        if url_parts.netloc and url_parts.netloc not in ("localhost", ".", "..", "-"):
            raise ValueError("file: URLs with hostname components are not permitted")

        # If the path is relative update it to be absolute
        if url_parts.netloc in (".", ".."):
            pwd = os.path.abspath(url_parts.netloc).replace(os.sep, "/") + "/"
            if is_win32:
                # prefix the path with a / in Windows
                pwd = f"/{pwd}"
            url_parts = url_parts._replace(path=urljoin(pwd, url_parts.path.lstrip("/")))

        resp = Response()
        resp.url = request.url

        # Open the file, translate certain errors into HTTP responses
        # Use urllib's unquote to translate percent escapes into whatever
        # they actually need to be
        try:
            # If the netloc is - then read from stdin
            if url_parts.netloc == "-":
                resp.raw = sys.stdin.buffer
                # make a fake response URL, the current directory
                resp.url = "file://" + os.path.abspath(".").replace(os.sep, "/") + "/"
            else:
                # Split the path on / (the URL directory separator) and decode any
                # % escapes in the parts
                path_parts = [unquote(p) for p in url_parts.path.split('/')]

                # Strip out the leading empty parts created from the leading /'s
                while path_parts and not path_parts[0]:
                    path_parts.pop(0)

                # If os.sep is in any of the parts, someone fed us some shenanigans.
                # Treat is like a missing file.
                if any(os.sep in p for p in path_parts):
                    raise IOError(errno.ENOENT, os.strerror(errno.ENOENT))

                # Look for a drive component. If one is present, store it separately
                # so that a directory separator can correctly be added to the real
                # path, and remove any empty path parts between the drive and the path.
                # Assume that a part ending with : or | (legacy) is a drive.
                if path_parts and (path_parts[0].endswith('|') or path_parts[0].endswith(':')):
                    path_drive = path_parts.pop(0)
                    if path_drive.endswith('|'):
                        path_drive = f"{path_drive[:-1]}:"

                    while path_parts and not path_parts[0]:
                        path_parts.pop(0)
                else:
                    path_drive = ''

                # Try to put the path back together
                # Join the drive back in, and stick os.sep in front of the path to
                # make it absolute.
                path = path_drive + os.sep + os.path.join(*path_parts)

                # Check if the drive assumptions above were correct. If path_drive
                # is set, and os.path.splitdrive does not return a drive, it wasn't
                # reall a drive. Put the path together again treating path_drive
                # as a normal path component.
                if path_drive and not os.path.splitdrive(path):
                    path = os.sep + os.path.join(path_drive, *path_parts)

                # Use io.open since we need to add a release_conn method, and
                # methods can't be added to file objects in python 2.
                resp.raw = io.open(path, "rb")
                resp.raw.release_conn = resp.raw.close
        except IOError as e:
            if e.errno == errno.EACCES:
                resp.status_code = codes.forbidden
            elif e.errno == errno.ENOENT:
                resp.status_code = codes.not_found
            else:
                resp.status_code = codes.bad_request

            # Wrap the error message in a file-like object
            # The error message will be localized, try to convert the string
            # representation of the exception into a byte stream
            resp_str = str(e).encode(locale.getpreferredencoding(False))
            resp.raw = BytesIO(resp_str)
            resp.headers['Content-Length'] = len(resp_str)

            # Add release_conn to the BytesIO object
            resp.raw.release_conn = resp.raw.close
        else:
            resp.status_code = codes.ok

            # If it's a regular file, set the Content-Length
            resp_stat = os.fstat(resp.raw.fileno())
            if stat.S_ISREG(resp_stat.st_mode):
                resp.headers['Content-length'] = resp_stat.st_size

        return resp
    
    xǁFileAdapterǁsend__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFileAdapterǁsend__mutmut_1': xǁFileAdapterǁsend__mutmut_1, 
        'xǁFileAdapterǁsend__mutmut_2': xǁFileAdapterǁsend__mutmut_2, 
        'xǁFileAdapterǁsend__mutmut_3': xǁFileAdapterǁsend__mutmut_3, 
        'xǁFileAdapterǁsend__mutmut_4': xǁFileAdapterǁsend__mutmut_4, 
        'xǁFileAdapterǁsend__mutmut_5': xǁFileAdapterǁsend__mutmut_5, 
        'xǁFileAdapterǁsend__mutmut_6': xǁFileAdapterǁsend__mutmut_6, 
        'xǁFileAdapterǁsend__mutmut_7': xǁFileAdapterǁsend__mutmut_7, 
        'xǁFileAdapterǁsend__mutmut_8': xǁFileAdapterǁsend__mutmut_8, 
        'xǁFileAdapterǁsend__mutmut_9': xǁFileAdapterǁsend__mutmut_9, 
        'xǁFileAdapterǁsend__mutmut_10': xǁFileAdapterǁsend__mutmut_10, 
        'xǁFileAdapterǁsend__mutmut_11': xǁFileAdapterǁsend__mutmut_11, 
        'xǁFileAdapterǁsend__mutmut_12': xǁFileAdapterǁsend__mutmut_12, 
        'xǁFileAdapterǁsend__mutmut_13': xǁFileAdapterǁsend__mutmut_13, 
        'xǁFileAdapterǁsend__mutmut_14': xǁFileAdapterǁsend__mutmut_14, 
        'xǁFileAdapterǁsend__mutmut_15': xǁFileAdapterǁsend__mutmut_15, 
        'xǁFileAdapterǁsend__mutmut_16': xǁFileAdapterǁsend__mutmut_16, 
        'xǁFileAdapterǁsend__mutmut_17': xǁFileAdapterǁsend__mutmut_17, 
        'xǁFileAdapterǁsend__mutmut_18': xǁFileAdapterǁsend__mutmut_18, 
        'xǁFileAdapterǁsend__mutmut_19': xǁFileAdapterǁsend__mutmut_19, 
        'xǁFileAdapterǁsend__mutmut_20': xǁFileAdapterǁsend__mutmut_20, 
        'xǁFileAdapterǁsend__mutmut_21': xǁFileAdapterǁsend__mutmut_21, 
        'xǁFileAdapterǁsend__mutmut_22': xǁFileAdapterǁsend__mutmut_22, 
        'xǁFileAdapterǁsend__mutmut_23': xǁFileAdapterǁsend__mutmut_23, 
        'xǁFileAdapterǁsend__mutmut_24': xǁFileAdapterǁsend__mutmut_24, 
        'xǁFileAdapterǁsend__mutmut_25': xǁFileAdapterǁsend__mutmut_25, 
        'xǁFileAdapterǁsend__mutmut_26': xǁFileAdapterǁsend__mutmut_26, 
        'xǁFileAdapterǁsend__mutmut_27': xǁFileAdapterǁsend__mutmut_27, 
        'xǁFileAdapterǁsend__mutmut_28': xǁFileAdapterǁsend__mutmut_28, 
        'xǁFileAdapterǁsend__mutmut_29': xǁFileAdapterǁsend__mutmut_29, 
        'xǁFileAdapterǁsend__mutmut_30': xǁFileAdapterǁsend__mutmut_30, 
        'xǁFileAdapterǁsend__mutmut_31': xǁFileAdapterǁsend__mutmut_31, 
        'xǁFileAdapterǁsend__mutmut_32': xǁFileAdapterǁsend__mutmut_32, 
        'xǁFileAdapterǁsend__mutmut_33': xǁFileAdapterǁsend__mutmut_33, 
        'xǁFileAdapterǁsend__mutmut_34': xǁFileAdapterǁsend__mutmut_34, 
        'xǁFileAdapterǁsend__mutmut_35': xǁFileAdapterǁsend__mutmut_35, 
        'xǁFileAdapterǁsend__mutmut_36': xǁFileAdapterǁsend__mutmut_36, 
        'xǁFileAdapterǁsend__mutmut_37': xǁFileAdapterǁsend__mutmut_37, 
        'xǁFileAdapterǁsend__mutmut_38': xǁFileAdapterǁsend__mutmut_38, 
        'xǁFileAdapterǁsend__mutmut_39': xǁFileAdapterǁsend__mutmut_39, 
        'xǁFileAdapterǁsend__mutmut_40': xǁFileAdapterǁsend__mutmut_40, 
        'xǁFileAdapterǁsend__mutmut_41': xǁFileAdapterǁsend__mutmut_41, 
        'xǁFileAdapterǁsend__mutmut_42': xǁFileAdapterǁsend__mutmut_42, 
        'xǁFileAdapterǁsend__mutmut_43': xǁFileAdapterǁsend__mutmut_43, 
        'xǁFileAdapterǁsend__mutmut_44': xǁFileAdapterǁsend__mutmut_44, 
        'xǁFileAdapterǁsend__mutmut_45': xǁFileAdapterǁsend__mutmut_45, 
        'xǁFileAdapterǁsend__mutmut_46': xǁFileAdapterǁsend__mutmut_46, 
        'xǁFileAdapterǁsend__mutmut_47': xǁFileAdapterǁsend__mutmut_47, 
        'xǁFileAdapterǁsend__mutmut_48': xǁFileAdapterǁsend__mutmut_48, 
        'xǁFileAdapterǁsend__mutmut_49': xǁFileAdapterǁsend__mutmut_49, 
        'xǁFileAdapterǁsend__mutmut_50': xǁFileAdapterǁsend__mutmut_50, 
        'xǁFileAdapterǁsend__mutmut_51': xǁFileAdapterǁsend__mutmut_51, 
        'xǁFileAdapterǁsend__mutmut_52': xǁFileAdapterǁsend__mutmut_52, 
        'xǁFileAdapterǁsend__mutmut_53': xǁFileAdapterǁsend__mutmut_53, 
        'xǁFileAdapterǁsend__mutmut_54': xǁFileAdapterǁsend__mutmut_54, 
        'xǁFileAdapterǁsend__mutmut_55': xǁFileAdapterǁsend__mutmut_55, 
        'xǁFileAdapterǁsend__mutmut_56': xǁFileAdapterǁsend__mutmut_56, 
        'xǁFileAdapterǁsend__mutmut_57': xǁFileAdapterǁsend__mutmut_57, 
        'xǁFileAdapterǁsend__mutmut_58': xǁFileAdapterǁsend__mutmut_58, 
        'xǁFileAdapterǁsend__mutmut_59': xǁFileAdapterǁsend__mutmut_59, 
        'xǁFileAdapterǁsend__mutmut_60': xǁFileAdapterǁsend__mutmut_60, 
        'xǁFileAdapterǁsend__mutmut_61': xǁFileAdapterǁsend__mutmut_61, 
        'xǁFileAdapterǁsend__mutmut_62': xǁFileAdapterǁsend__mutmut_62, 
        'xǁFileAdapterǁsend__mutmut_63': xǁFileAdapterǁsend__mutmut_63, 
        'xǁFileAdapterǁsend__mutmut_64': xǁFileAdapterǁsend__mutmut_64, 
        'xǁFileAdapterǁsend__mutmut_65': xǁFileAdapterǁsend__mutmut_65, 
        'xǁFileAdapterǁsend__mutmut_66': xǁFileAdapterǁsend__mutmut_66, 
        'xǁFileAdapterǁsend__mutmut_67': xǁFileAdapterǁsend__mutmut_67, 
        'xǁFileAdapterǁsend__mutmut_68': xǁFileAdapterǁsend__mutmut_68, 
        'xǁFileAdapterǁsend__mutmut_69': xǁFileAdapterǁsend__mutmut_69, 
        'xǁFileAdapterǁsend__mutmut_70': xǁFileAdapterǁsend__mutmut_70, 
        'xǁFileAdapterǁsend__mutmut_71': xǁFileAdapterǁsend__mutmut_71, 
        'xǁFileAdapterǁsend__mutmut_72': xǁFileAdapterǁsend__mutmut_72, 
        'xǁFileAdapterǁsend__mutmut_73': xǁFileAdapterǁsend__mutmut_73, 
        'xǁFileAdapterǁsend__mutmut_74': xǁFileAdapterǁsend__mutmut_74, 
        'xǁFileAdapterǁsend__mutmut_75': xǁFileAdapterǁsend__mutmut_75, 
        'xǁFileAdapterǁsend__mutmut_76': xǁFileAdapterǁsend__mutmut_76, 
        'xǁFileAdapterǁsend__mutmut_77': xǁFileAdapterǁsend__mutmut_77, 
        'xǁFileAdapterǁsend__mutmut_78': xǁFileAdapterǁsend__mutmut_78, 
        'xǁFileAdapterǁsend__mutmut_79': xǁFileAdapterǁsend__mutmut_79, 
        'xǁFileAdapterǁsend__mutmut_80': xǁFileAdapterǁsend__mutmut_80, 
        'xǁFileAdapterǁsend__mutmut_81': xǁFileAdapterǁsend__mutmut_81, 
        'xǁFileAdapterǁsend__mutmut_82': xǁFileAdapterǁsend__mutmut_82, 
        'xǁFileAdapterǁsend__mutmut_83': xǁFileAdapterǁsend__mutmut_83, 
        'xǁFileAdapterǁsend__mutmut_84': xǁFileAdapterǁsend__mutmut_84, 
        'xǁFileAdapterǁsend__mutmut_85': xǁFileAdapterǁsend__mutmut_85, 
        'xǁFileAdapterǁsend__mutmut_86': xǁFileAdapterǁsend__mutmut_86, 
        'xǁFileAdapterǁsend__mutmut_87': xǁFileAdapterǁsend__mutmut_87, 
        'xǁFileAdapterǁsend__mutmut_88': xǁFileAdapterǁsend__mutmut_88, 
        'xǁFileAdapterǁsend__mutmut_89': xǁFileAdapterǁsend__mutmut_89, 
        'xǁFileAdapterǁsend__mutmut_90': xǁFileAdapterǁsend__mutmut_90, 
        'xǁFileAdapterǁsend__mutmut_91': xǁFileAdapterǁsend__mutmut_91, 
        'xǁFileAdapterǁsend__mutmut_92': xǁFileAdapterǁsend__mutmut_92, 
        'xǁFileAdapterǁsend__mutmut_93': xǁFileAdapterǁsend__mutmut_93, 
        'xǁFileAdapterǁsend__mutmut_94': xǁFileAdapterǁsend__mutmut_94, 
        'xǁFileAdapterǁsend__mutmut_95': xǁFileAdapterǁsend__mutmut_95, 
        'xǁFileAdapterǁsend__mutmut_96': xǁFileAdapterǁsend__mutmut_96, 
        'xǁFileAdapterǁsend__mutmut_97': xǁFileAdapterǁsend__mutmut_97, 
        'xǁFileAdapterǁsend__mutmut_98': xǁFileAdapterǁsend__mutmut_98, 
        'xǁFileAdapterǁsend__mutmut_99': xǁFileAdapterǁsend__mutmut_99, 
        'xǁFileAdapterǁsend__mutmut_100': xǁFileAdapterǁsend__mutmut_100, 
        'xǁFileAdapterǁsend__mutmut_101': xǁFileAdapterǁsend__mutmut_101, 
        'xǁFileAdapterǁsend__mutmut_102': xǁFileAdapterǁsend__mutmut_102, 
        'xǁFileAdapterǁsend__mutmut_103': xǁFileAdapterǁsend__mutmut_103, 
        'xǁFileAdapterǁsend__mutmut_104': xǁFileAdapterǁsend__mutmut_104, 
        'xǁFileAdapterǁsend__mutmut_105': xǁFileAdapterǁsend__mutmut_105, 
        'xǁFileAdapterǁsend__mutmut_106': xǁFileAdapterǁsend__mutmut_106, 
        'xǁFileAdapterǁsend__mutmut_107': xǁFileAdapterǁsend__mutmut_107, 
        'xǁFileAdapterǁsend__mutmut_108': xǁFileAdapterǁsend__mutmut_108, 
        'xǁFileAdapterǁsend__mutmut_109': xǁFileAdapterǁsend__mutmut_109, 
        'xǁFileAdapterǁsend__mutmut_110': xǁFileAdapterǁsend__mutmut_110, 
        'xǁFileAdapterǁsend__mutmut_111': xǁFileAdapterǁsend__mutmut_111, 
        'xǁFileAdapterǁsend__mutmut_112': xǁFileAdapterǁsend__mutmut_112, 
        'xǁFileAdapterǁsend__mutmut_113': xǁFileAdapterǁsend__mutmut_113, 
        'xǁFileAdapterǁsend__mutmut_114': xǁFileAdapterǁsend__mutmut_114, 
        'xǁFileAdapterǁsend__mutmut_115': xǁFileAdapterǁsend__mutmut_115, 
        'xǁFileAdapterǁsend__mutmut_116': xǁFileAdapterǁsend__mutmut_116, 
        'xǁFileAdapterǁsend__mutmut_117': xǁFileAdapterǁsend__mutmut_117, 
        'xǁFileAdapterǁsend__mutmut_118': xǁFileAdapterǁsend__mutmut_118, 
        'xǁFileAdapterǁsend__mutmut_119': xǁFileAdapterǁsend__mutmut_119, 
        'xǁFileAdapterǁsend__mutmut_120': xǁFileAdapterǁsend__mutmut_120, 
        'xǁFileAdapterǁsend__mutmut_121': xǁFileAdapterǁsend__mutmut_121, 
        'xǁFileAdapterǁsend__mutmut_122': xǁFileAdapterǁsend__mutmut_122, 
        'xǁFileAdapterǁsend__mutmut_123': xǁFileAdapterǁsend__mutmut_123, 
        'xǁFileAdapterǁsend__mutmut_124': xǁFileAdapterǁsend__mutmut_124, 
        'xǁFileAdapterǁsend__mutmut_125': xǁFileAdapterǁsend__mutmut_125, 
        'xǁFileAdapterǁsend__mutmut_126': xǁFileAdapterǁsend__mutmut_126, 
        'xǁFileAdapterǁsend__mutmut_127': xǁFileAdapterǁsend__mutmut_127, 
        'xǁFileAdapterǁsend__mutmut_128': xǁFileAdapterǁsend__mutmut_128, 
        'xǁFileAdapterǁsend__mutmut_129': xǁFileAdapterǁsend__mutmut_129, 
        'xǁFileAdapterǁsend__mutmut_130': xǁFileAdapterǁsend__mutmut_130, 
        'xǁFileAdapterǁsend__mutmut_131': xǁFileAdapterǁsend__mutmut_131, 
        'xǁFileAdapterǁsend__mutmut_132': xǁFileAdapterǁsend__mutmut_132, 
        'xǁFileAdapterǁsend__mutmut_133': xǁFileAdapterǁsend__mutmut_133, 
        'xǁFileAdapterǁsend__mutmut_134': xǁFileAdapterǁsend__mutmut_134, 
        'xǁFileAdapterǁsend__mutmut_135': xǁFileAdapterǁsend__mutmut_135, 
        'xǁFileAdapterǁsend__mutmut_136': xǁFileAdapterǁsend__mutmut_136, 
        'xǁFileAdapterǁsend__mutmut_137': xǁFileAdapterǁsend__mutmut_137, 
        'xǁFileAdapterǁsend__mutmut_138': xǁFileAdapterǁsend__mutmut_138, 
        'xǁFileAdapterǁsend__mutmut_139': xǁFileAdapterǁsend__mutmut_139, 
        'xǁFileAdapterǁsend__mutmut_140': xǁFileAdapterǁsend__mutmut_140, 
        'xǁFileAdapterǁsend__mutmut_141': xǁFileAdapterǁsend__mutmut_141, 
        'xǁFileAdapterǁsend__mutmut_142': xǁFileAdapterǁsend__mutmut_142, 
        'xǁFileAdapterǁsend__mutmut_143': xǁFileAdapterǁsend__mutmut_143, 
        'xǁFileAdapterǁsend__mutmut_144': xǁFileAdapterǁsend__mutmut_144, 
        'xǁFileAdapterǁsend__mutmut_145': xǁFileAdapterǁsend__mutmut_145, 
        'xǁFileAdapterǁsend__mutmut_146': xǁFileAdapterǁsend__mutmut_146, 
        'xǁFileAdapterǁsend__mutmut_147': xǁFileAdapterǁsend__mutmut_147, 
        'xǁFileAdapterǁsend__mutmut_148': xǁFileAdapterǁsend__mutmut_148, 
        'xǁFileAdapterǁsend__mutmut_149': xǁFileAdapterǁsend__mutmut_149, 
        'xǁFileAdapterǁsend__mutmut_150': xǁFileAdapterǁsend__mutmut_150, 
        'xǁFileAdapterǁsend__mutmut_151': xǁFileAdapterǁsend__mutmut_151, 
        'xǁFileAdapterǁsend__mutmut_152': xǁFileAdapterǁsend__mutmut_152, 
        'xǁFileAdapterǁsend__mutmut_153': xǁFileAdapterǁsend__mutmut_153, 
        'xǁFileAdapterǁsend__mutmut_154': xǁFileAdapterǁsend__mutmut_154, 
        'xǁFileAdapterǁsend__mutmut_155': xǁFileAdapterǁsend__mutmut_155, 
        'xǁFileAdapterǁsend__mutmut_156': xǁFileAdapterǁsend__mutmut_156, 
        'xǁFileAdapterǁsend__mutmut_157': xǁFileAdapterǁsend__mutmut_157, 
        'xǁFileAdapterǁsend__mutmut_158': xǁFileAdapterǁsend__mutmut_158, 
        'xǁFileAdapterǁsend__mutmut_159': xǁFileAdapterǁsend__mutmut_159, 
        'xǁFileAdapterǁsend__mutmut_160': xǁFileAdapterǁsend__mutmut_160
    }
    
    def send(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFileAdapterǁsend__mutmut_orig"), object.__getattribute__(self, "xǁFileAdapterǁsend__mutmut_mutants"), args, kwargs, self)
        return result 
    
    send.__signature__ = _mutmut_signature(xǁFileAdapterǁsend__mutmut_orig)
    xǁFileAdapterǁsend__mutmut_orig.__name__ = 'xǁFileAdapterǁsend'

    def close(self):
        pass

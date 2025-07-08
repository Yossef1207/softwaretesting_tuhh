from __future__ import annotations

import copy
import itertools
import logging
from collections import defaultdict
from collections.abc import Mapping
from contextlib import contextmanager, suppress
from datetime import datetime
from time import time
from typing import Any

from requests import Response

from streamlink.exceptions import PluginError, StreamError
from streamlink.session import Streamlink
from streamlink.stream.dash.manifest import MPD, Representation, freeze_timeline
from streamlink.stream.dash.segment import DASHSegment
from streamlink.stream.ffmpegmux import FFMPEGMuxer
from streamlink.stream.segmented import SegmentedStreamReader, SegmentedStreamWorker, SegmentedStreamWriter
from streamlink.stream.stream import Stream
from streamlink.utils.l10n import Language
from streamlink.utils.parse import parse_xml
from streamlink.utils.times import now


log = logging.getLogger(".".join(__name__.split(".")[:-1]))
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


class DASHStreamWriter(SegmentedStreamWriter[DASHSegment, Response]):
    reader: DASHStreamReader
    stream: DASHStream

    def xǁDASHStreamWriterǁfetch__mutmut_orig(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_1(self, segment: DASHSegment):
        if self.closed:
            return

        name = None
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_2(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = None
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_3(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in >= 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_4(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 1:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_5(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(None)
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_6(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_7(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(None):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_8(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(None)
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_9(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(None)

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_10(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = None
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_11(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(None)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_12(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.copy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_13(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = None

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_14(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop(None, {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_15(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", None)

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_16(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop({})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_17(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", )

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_18(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("XXheadersXX", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_19(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("HEADERS", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_20(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("Headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_21(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = None
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_22(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = None
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_23(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(None) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_24(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start - length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_25(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length + 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_26(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 2) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_27(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else "XXXX"
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_28(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = None

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_29(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["XXRangeXX"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_30(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_31(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["RANGE"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_32(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                None,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_33(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=None,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_34(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=None,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_35(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=None,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_36(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=None,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_37(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_38(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_39(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_40(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_41(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                **request_args,
            )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_42(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                )
        except StreamError as err:
            log.error(f"{self.reader.mime_type} segment {name}: failed ({err})")

    def xǁDASHStreamWriterǁfetch__mutmut_43(self, segment: DASHSegment):
        if self.closed:
            return

        name = segment.name
        available_in = segment.available_in
        if available_in > 0:
            log.debug(f"{self.reader.mime_type} segment {name}: waiting {available_in:.01f}s ({segment.availability})")
            if not self.wait(available_in):
                log.debug(f"{self.reader.mime_type} segment {name}: cancelled")
                return
        log.debug(f"{self.reader.mime_type} segment {name}: downloading ({segment.availability})")

        request_args = copy.deepcopy(self.reader.stream.args)
        headers = request_args.pop("headers", {})

        if segment.byterange:
            start, length = segment.byterange
            end = str(start + length - 1) if length else ""
            headers["Range"] = f"bytes={start}-{end}"

        try:
            return self.session.http.get(
                segment.uri,
                timeout=self.timeout,
                exception=StreamError,
                headers=headers,
                retries=self.retries,
                **request_args,
            )
        except StreamError as err:
            log.error(None)
    
    xǁDASHStreamWriterǁfetch__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamWriterǁfetch__mutmut_1': xǁDASHStreamWriterǁfetch__mutmut_1, 
        'xǁDASHStreamWriterǁfetch__mutmut_2': xǁDASHStreamWriterǁfetch__mutmut_2, 
        'xǁDASHStreamWriterǁfetch__mutmut_3': xǁDASHStreamWriterǁfetch__mutmut_3, 
        'xǁDASHStreamWriterǁfetch__mutmut_4': xǁDASHStreamWriterǁfetch__mutmut_4, 
        'xǁDASHStreamWriterǁfetch__mutmut_5': xǁDASHStreamWriterǁfetch__mutmut_5, 
        'xǁDASHStreamWriterǁfetch__mutmut_6': xǁDASHStreamWriterǁfetch__mutmut_6, 
        'xǁDASHStreamWriterǁfetch__mutmut_7': xǁDASHStreamWriterǁfetch__mutmut_7, 
        'xǁDASHStreamWriterǁfetch__mutmut_8': xǁDASHStreamWriterǁfetch__mutmut_8, 
        'xǁDASHStreamWriterǁfetch__mutmut_9': xǁDASHStreamWriterǁfetch__mutmut_9, 
        'xǁDASHStreamWriterǁfetch__mutmut_10': xǁDASHStreamWriterǁfetch__mutmut_10, 
        'xǁDASHStreamWriterǁfetch__mutmut_11': xǁDASHStreamWriterǁfetch__mutmut_11, 
        'xǁDASHStreamWriterǁfetch__mutmut_12': xǁDASHStreamWriterǁfetch__mutmut_12, 
        'xǁDASHStreamWriterǁfetch__mutmut_13': xǁDASHStreamWriterǁfetch__mutmut_13, 
        'xǁDASHStreamWriterǁfetch__mutmut_14': xǁDASHStreamWriterǁfetch__mutmut_14, 
        'xǁDASHStreamWriterǁfetch__mutmut_15': xǁDASHStreamWriterǁfetch__mutmut_15, 
        'xǁDASHStreamWriterǁfetch__mutmut_16': xǁDASHStreamWriterǁfetch__mutmut_16, 
        'xǁDASHStreamWriterǁfetch__mutmut_17': xǁDASHStreamWriterǁfetch__mutmut_17, 
        'xǁDASHStreamWriterǁfetch__mutmut_18': xǁDASHStreamWriterǁfetch__mutmut_18, 
        'xǁDASHStreamWriterǁfetch__mutmut_19': xǁDASHStreamWriterǁfetch__mutmut_19, 
        'xǁDASHStreamWriterǁfetch__mutmut_20': xǁDASHStreamWriterǁfetch__mutmut_20, 
        'xǁDASHStreamWriterǁfetch__mutmut_21': xǁDASHStreamWriterǁfetch__mutmut_21, 
        'xǁDASHStreamWriterǁfetch__mutmut_22': xǁDASHStreamWriterǁfetch__mutmut_22, 
        'xǁDASHStreamWriterǁfetch__mutmut_23': xǁDASHStreamWriterǁfetch__mutmut_23, 
        'xǁDASHStreamWriterǁfetch__mutmut_24': xǁDASHStreamWriterǁfetch__mutmut_24, 
        'xǁDASHStreamWriterǁfetch__mutmut_25': xǁDASHStreamWriterǁfetch__mutmut_25, 
        'xǁDASHStreamWriterǁfetch__mutmut_26': xǁDASHStreamWriterǁfetch__mutmut_26, 
        'xǁDASHStreamWriterǁfetch__mutmut_27': xǁDASHStreamWriterǁfetch__mutmut_27, 
        'xǁDASHStreamWriterǁfetch__mutmut_28': xǁDASHStreamWriterǁfetch__mutmut_28, 
        'xǁDASHStreamWriterǁfetch__mutmut_29': xǁDASHStreamWriterǁfetch__mutmut_29, 
        'xǁDASHStreamWriterǁfetch__mutmut_30': xǁDASHStreamWriterǁfetch__mutmut_30, 
        'xǁDASHStreamWriterǁfetch__mutmut_31': xǁDASHStreamWriterǁfetch__mutmut_31, 
        'xǁDASHStreamWriterǁfetch__mutmut_32': xǁDASHStreamWriterǁfetch__mutmut_32, 
        'xǁDASHStreamWriterǁfetch__mutmut_33': xǁDASHStreamWriterǁfetch__mutmut_33, 
        'xǁDASHStreamWriterǁfetch__mutmut_34': xǁDASHStreamWriterǁfetch__mutmut_34, 
        'xǁDASHStreamWriterǁfetch__mutmut_35': xǁDASHStreamWriterǁfetch__mutmut_35, 
        'xǁDASHStreamWriterǁfetch__mutmut_36': xǁDASHStreamWriterǁfetch__mutmut_36, 
        'xǁDASHStreamWriterǁfetch__mutmut_37': xǁDASHStreamWriterǁfetch__mutmut_37, 
        'xǁDASHStreamWriterǁfetch__mutmut_38': xǁDASHStreamWriterǁfetch__mutmut_38, 
        'xǁDASHStreamWriterǁfetch__mutmut_39': xǁDASHStreamWriterǁfetch__mutmut_39, 
        'xǁDASHStreamWriterǁfetch__mutmut_40': xǁDASHStreamWriterǁfetch__mutmut_40, 
        'xǁDASHStreamWriterǁfetch__mutmut_41': xǁDASHStreamWriterǁfetch__mutmut_41, 
        'xǁDASHStreamWriterǁfetch__mutmut_42': xǁDASHStreamWriterǁfetch__mutmut_42, 
        'xǁDASHStreamWriterǁfetch__mutmut_43': xǁDASHStreamWriterǁfetch__mutmut_43
    }
    
    def fetch(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamWriterǁfetch__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamWriterǁfetch__mutmut_mutants"), args, kwargs, self)
        return result 
    
    fetch.__signature__ = _mutmut_signature(xǁDASHStreamWriterǁfetch__mutmut_orig)
    xǁDASHStreamWriterǁfetch__mutmut_orig.__name__ = 'xǁDASHStreamWriterǁfetch'

    def xǁDASHStreamWriterǁwrite__mutmut_orig(self, segment, res, chunk_size=8192):
        for chunk in res.iter_content(chunk_size):
            if self.closed:
                log.warning(f"{self.reader.mime_type} segment {segment.name}: aborted")
                return
            self.reader.buffer.write(chunk)

        log.debug(f"{self.reader.mime_type} segment {segment.name}: completed")

    def xǁDASHStreamWriterǁwrite__mutmut_1(self, segment, res, chunk_size=8193):
        for chunk in res.iter_content(chunk_size):
            if self.closed:
                log.warning(f"{self.reader.mime_type} segment {segment.name}: aborted")
                return
            self.reader.buffer.write(chunk)

        log.debug(f"{self.reader.mime_type} segment {segment.name}: completed")

    def xǁDASHStreamWriterǁwrite__mutmut_2(self, segment, res, chunk_size=8192):
        for chunk in res.iter_content(None):
            if self.closed:
                log.warning(f"{self.reader.mime_type} segment {segment.name}: aborted")
                return
            self.reader.buffer.write(chunk)

        log.debug(f"{self.reader.mime_type} segment {segment.name}: completed")

    def xǁDASHStreamWriterǁwrite__mutmut_3(self, segment, res, chunk_size=8192):
        for chunk in res.iter_content(chunk_size):
            if self.closed:
                log.warning(None)
                return
            self.reader.buffer.write(chunk)

        log.debug(f"{self.reader.mime_type} segment {segment.name}: completed")

    def xǁDASHStreamWriterǁwrite__mutmut_4(self, segment, res, chunk_size=8192):
        for chunk in res.iter_content(chunk_size):
            if self.closed:
                log.warning(f"{self.reader.mime_type} segment {segment.name}: aborted")
                return
            self.reader.buffer.write(None)

        log.debug(f"{self.reader.mime_type} segment {segment.name}: completed")

    def xǁDASHStreamWriterǁwrite__mutmut_5(self, segment, res, chunk_size=8192):
        for chunk in res.iter_content(chunk_size):
            if self.closed:
                log.warning(f"{self.reader.mime_type} segment {segment.name}: aborted")
                return
            self.reader.buffer.write(chunk)

        log.debug(None)
    
    xǁDASHStreamWriterǁwrite__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamWriterǁwrite__mutmut_1': xǁDASHStreamWriterǁwrite__mutmut_1, 
        'xǁDASHStreamWriterǁwrite__mutmut_2': xǁDASHStreamWriterǁwrite__mutmut_2, 
        'xǁDASHStreamWriterǁwrite__mutmut_3': xǁDASHStreamWriterǁwrite__mutmut_3, 
        'xǁDASHStreamWriterǁwrite__mutmut_4': xǁDASHStreamWriterǁwrite__mutmut_4, 
        'xǁDASHStreamWriterǁwrite__mutmut_5': xǁDASHStreamWriterǁwrite__mutmut_5
    }
    
    def write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamWriterǁwrite__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamWriterǁwrite__mutmut_mutants"), args, kwargs, self)
        return result 
    
    write.__signature__ = _mutmut_signature(xǁDASHStreamWriterǁwrite__mutmut_orig)
    xǁDASHStreamWriterǁwrite__mutmut_orig.__name__ = 'xǁDASHStreamWriterǁwrite'


class DASHStreamWorker(SegmentedStreamWorker[DASHSegment, Response]):
    reader: DASHStreamReader
    writer: DASHStreamWriter
    stream: DASHStream

    def xǁDASHStreamWorkerǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("dash-manifest-reload-attempts")

    def xǁDASHStreamWorkerǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("dash-manifest-reload-attempts")

    def xǁDASHStreamWorkerǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("dash-manifest-reload-attempts")

    def xǁDASHStreamWorkerǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = None

        self.manifest_reload_retries = self.session.options.get("dash-manifest-reload-attempts")

    def xǁDASHStreamWorkerǁ__init____mutmut_4(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = None

    def xǁDASHStreamWorkerǁ__init____mutmut_5(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get(None)

    def xǁDASHStreamWorkerǁ__init____mutmut_6(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("XXdash-manifest-reload-attemptsXX")

    def xǁDASHStreamWorkerǁ__init____mutmut_7(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("DASH-MANIFEST-RELOAD-ATTEMPTS")

    def xǁDASHStreamWorkerǁ__init____mutmut_8(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mpd = self.stream.mpd

        self.manifest_reload_retries = self.session.options.get("Dash-manifest-reload-attempts")
    
    xǁDASHStreamWorkerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamWorkerǁ__init____mutmut_1': xǁDASHStreamWorkerǁ__init____mutmut_1, 
        'xǁDASHStreamWorkerǁ__init____mutmut_2': xǁDASHStreamWorkerǁ__init____mutmut_2, 
        'xǁDASHStreamWorkerǁ__init____mutmut_3': xǁDASHStreamWorkerǁ__init____mutmut_3, 
        'xǁDASHStreamWorkerǁ__init____mutmut_4': xǁDASHStreamWorkerǁ__init____mutmut_4, 
        'xǁDASHStreamWorkerǁ__init____mutmut_5': xǁDASHStreamWorkerǁ__init____mutmut_5, 
        'xǁDASHStreamWorkerǁ__init____mutmut_6': xǁDASHStreamWorkerǁ__init____mutmut_6, 
        'xǁDASHStreamWorkerǁ__init____mutmut_7': xǁDASHStreamWorkerǁ__init____mutmut_7, 
        'xǁDASHStreamWorkerǁ__init____mutmut_8': xǁDASHStreamWorkerǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamWorkerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamWorkerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁDASHStreamWorkerǁ__init____mutmut_orig)
    xǁDASHStreamWorkerǁ__init____mutmut_orig.__name__ = 'xǁDASHStreamWorkerǁ__init__'

    @contextmanager
    def sleeper(self, duration):
        """
        Do something and then wait for a given duration minus the time it took doing something
        """
        s = time()
        yield
        time_to_sleep = duration - (time() - s)
        if time_to_sleep > 0:
            self.wait(time_to_sleep)

    def xǁDASHStreamWorkerǁiter_segments__mutmut_orig(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_1(self):
        init = None
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_2(self):
        init = False
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_3(self):
        init = True
        back_off_factor = None
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_4(self):
        init = True
        back_off_factor = 2
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_5(self):
        init = True
        back_off_factor = 1
        while self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_6(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = None

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_7(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(None)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_8(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type != "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_9(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "XXstaticXX":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_10(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "STATIC":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_11(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "Static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_12(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = None
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_13(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 6
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_14(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = None

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_15(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        None,
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_16(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        None,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_17(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_18(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_19(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 1,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_20(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    ) and 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_21(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 6
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_22(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(None):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_23(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait / back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_24(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_25(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    break

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_26(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = None
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_27(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=None,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_28(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_29(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_30(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_31(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        return
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_32(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type == "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_33(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "XXdynamicXX":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_34(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "DYNAMIC":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_35(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "Dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_36(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_37(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = None
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_38(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(None, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_39(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, None)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_40(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_41(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, )
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_42(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor / 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_43(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 2.3, 10.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_44(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 11.0)
                else:
                    back_off_factor = 1

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_45(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = None

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_46(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 2

                init = False

    def xǁDASHStreamWorkerǁiter_segments__mutmut_47(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = None

    def xǁDASHStreamWorkerǁiter_segments__mutmut_48(self):
        init = True
        back_off_factor = 1
        while not self.closed:
            # find the representation by ID
            representation = self.mpd.get_representation(self.reader.ident)

            if self.mpd.type == "static":
                refresh_wait = 5
            else:
                refresh_wait = (
                    max(
                        self.mpd.minimumUpdatePeriod.total_seconds(),
                        representation.period.duration.total_seconds() if representation else 0,
                    )
                    or 5
                )

            with self.sleeper(refresh_wait * back_off_factor):
                if not representation:
                    continue

                iter_segments = representation.segments(
                    init=init,
                    # sync initial timeline generation between audio and video threads
                    timestamp=self.reader.timestamp if init else None,
                )
                for segment in iter_segments:
                    if self.closed:
                        break
                    yield segment

                # close worker if type is not dynamic (all segments were put into writer queue)
                if self.mpd.type != "dynamic":
                    self.close()
                    return

                if not self.reload():
                    back_off_factor = max(back_off_factor * 1.3, 10.0)
                else:
                    back_off_factor = 1

                init = True
    
    xǁDASHStreamWorkerǁiter_segments__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamWorkerǁiter_segments__mutmut_1': xǁDASHStreamWorkerǁiter_segments__mutmut_1, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_2': xǁDASHStreamWorkerǁiter_segments__mutmut_2, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_3': xǁDASHStreamWorkerǁiter_segments__mutmut_3, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_4': xǁDASHStreamWorkerǁiter_segments__mutmut_4, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_5': xǁDASHStreamWorkerǁiter_segments__mutmut_5, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_6': xǁDASHStreamWorkerǁiter_segments__mutmut_6, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_7': xǁDASHStreamWorkerǁiter_segments__mutmut_7, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_8': xǁDASHStreamWorkerǁiter_segments__mutmut_8, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_9': xǁDASHStreamWorkerǁiter_segments__mutmut_9, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_10': xǁDASHStreamWorkerǁiter_segments__mutmut_10, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_11': xǁDASHStreamWorkerǁiter_segments__mutmut_11, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_12': xǁDASHStreamWorkerǁiter_segments__mutmut_12, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_13': xǁDASHStreamWorkerǁiter_segments__mutmut_13, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_14': xǁDASHStreamWorkerǁiter_segments__mutmut_14, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_15': xǁDASHStreamWorkerǁiter_segments__mutmut_15, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_16': xǁDASHStreamWorkerǁiter_segments__mutmut_16, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_17': xǁDASHStreamWorkerǁiter_segments__mutmut_17, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_18': xǁDASHStreamWorkerǁiter_segments__mutmut_18, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_19': xǁDASHStreamWorkerǁiter_segments__mutmut_19, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_20': xǁDASHStreamWorkerǁiter_segments__mutmut_20, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_21': xǁDASHStreamWorkerǁiter_segments__mutmut_21, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_22': xǁDASHStreamWorkerǁiter_segments__mutmut_22, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_23': xǁDASHStreamWorkerǁiter_segments__mutmut_23, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_24': xǁDASHStreamWorkerǁiter_segments__mutmut_24, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_25': xǁDASHStreamWorkerǁiter_segments__mutmut_25, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_26': xǁDASHStreamWorkerǁiter_segments__mutmut_26, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_27': xǁDASHStreamWorkerǁiter_segments__mutmut_27, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_28': xǁDASHStreamWorkerǁiter_segments__mutmut_28, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_29': xǁDASHStreamWorkerǁiter_segments__mutmut_29, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_30': xǁDASHStreamWorkerǁiter_segments__mutmut_30, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_31': xǁDASHStreamWorkerǁiter_segments__mutmut_31, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_32': xǁDASHStreamWorkerǁiter_segments__mutmut_32, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_33': xǁDASHStreamWorkerǁiter_segments__mutmut_33, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_34': xǁDASHStreamWorkerǁiter_segments__mutmut_34, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_35': xǁDASHStreamWorkerǁiter_segments__mutmut_35, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_36': xǁDASHStreamWorkerǁiter_segments__mutmut_36, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_37': xǁDASHStreamWorkerǁiter_segments__mutmut_37, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_38': xǁDASHStreamWorkerǁiter_segments__mutmut_38, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_39': xǁDASHStreamWorkerǁiter_segments__mutmut_39, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_40': xǁDASHStreamWorkerǁiter_segments__mutmut_40, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_41': xǁDASHStreamWorkerǁiter_segments__mutmut_41, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_42': xǁDASHStreamWorkerǁiter_segments__mutmut_42, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_43': xǁDASHStreamWorkerǁiter_segments__mutmut_43, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_44': xǁDASHStreamWorkerǁiter_segments__mutmut_44, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_45': xǁDASHStreamWorkerǁiter_segments__mutmut_45, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_46': xǁDASHStreamWorkerǁiter_segments__mutmut_46, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_47': xǁDASHStreamWorkerǁiter_segments__mutmut_47, 
        'xǁDASHStreamWorkerǁiter_segments__mutmut_48': xǁDASHStreamWorkerǁiter_segments__mutmut_48
    }
    
    def iter_segments(self, *args, **kwargs):
        result = yield from _mutmut_yield_from_trampoline(object.__getattribute__(self, "xǁDASHStreamWorkerǁiter_segments__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamWorkerǁiter_segments__mutmut_mutants"), args, kwargs, self)
        return result 
    
    iter_segments.__signature__ = _mutmut_signature(xǁDASHStreamWorkerǁiter_segments__mutmut_orig)
    xǁDASHStreamWorkerǁiter_segments__mutmut_orig.__name__ = 'xǁDASHStreamWorkerǁiter_segments'

    def xǁDASHStreamWorkerǁreload__mutmut_orig(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_1(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(None)
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_2(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = None

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_3(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            None,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_4(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=None,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_5(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=None,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_6(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_7(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_8(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_9(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_10(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = None

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_11(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            None,
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_12(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=None,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_13(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=None,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_14(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=None,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_15(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_16(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_17(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_18(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_19(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(None, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_20(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=None),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_21(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_22(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_23(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=False),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_24(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = None
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_25(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(None)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_26(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(None):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_27(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = None

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_28(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) >= 0

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_29(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 1

        if changed:
            self.mpd = new_mpd

        return changed

    def xǁDASHStreamWorkerǁreload__mutmut_30(self):
        if self.closed:
            return

        self.reader.buffer.wait_free()
        log.debug(f"Reloading manifest {self.reader.ident!r}")
        res = self.session.http.get(
            self.mpd.url,
            exception=StreamError,
            retries=self.manifest_reload_retries,
            **self.stream.args,
        )

        new_mpd = MPD(
            self.session.http.xml(res, ignore_ns=True),
            base_url=self.mpd.base_url,
            url=self.mpd.url,
            timelines=self.mpd.timelines,
        )

        new_rep = new_mpd.get_representation(self.reader.ident)
        with freeze_timeline(new_mpd):
            changed = len(list(itertools.islice(new_rep.segments(), 1))) > 0

        if changed:
            self.mpd = None

        return changed
    
    xǁDASHStreamWorkerǁreload__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamWorkerǁreload__mutmut_1': xǁDASHStreamWorkerǁreload__mutmut_1, 
        'xǁDASHStreamWorkerǁreload__mutmut_2': xǁDASHStreamWorkerǁreload__mutmut_2, 
        'xǁDASHStreamWorkerǁreload__mutmut_3': xǁDASHStreamWorkerǁreload__mutmut_3, 
        'xǁDASHStreamWorkerǁreload__mutmut_4': xǁDASHStreamWorkerǁreload__mutmut_4, 
        'xǁDASHStreamWorkerǁreload__mutmut_5': xǁDASHStreamWorkerǁreload__mutmut_5, 
        'xǁDASHStreamWorkerǁreload__mutmut_6': xǁDASHStreamWorkerǁreload__mutmut_6, 
        'xǁDASHStreamWorkerǁreload__mutmut_7': xǁDASHStreamWorkerǁreload__mutmut_7, 
        'xǁDASHStreamWorkerǁreload__mutmut_8': xǁDASHStreamWorkerǁreload__mutmut_8, 
        'xǁDASHStreamWorkerǁreload__mutmut_9': xǁDASHStreamWorkerǁreload__mutmut_9, 
        'xǁDASHStreamWorkerǁreload__mutmut_10': xǁDASHStreamWorkerǁreload__mutmut_10, 
        'xǁDASHStreamWorkerǁreload__mutmut_11': xǁDASHStreamWorkerǁreload__mutmut_11, 
        'xǁDASHStreamWorkerǁreload__mutmut_12': xǁDASHStreamWorkerǁreload__mutmut_12, 
        'xǁDASHStreamWorkerǁreload__mutmut_13': xǁDASHStreamWorkerǁreload__mutmut_13, 
        'xǁDASHStreamWorkerǁreload__mutmut_14': xǁDASHStreamWorkerǁreload__mutmut_14, 
        'xǁDASHStreamWorkerǁreload__mutmut_15': xǁDASHStreamWorkerǁreload__mutmut_15, 
        'xǁDASHStreamWorkerǁreload__mutmut_16': xǁDASHStreamWorkerǁreload__mutmut_16, 
        'xǁDASHStreamWorkerǁreload__mutmut_17': xǁDASHStreamWorkerǁreload__mutmut_17, 
        'xǁDASHStreamWorkerǁreload__mutmut_18': xǁDASHStreamWorkerǁreload__mutmut_18, 
        'xǁDASHStreamWorkerǁreload__mutmut_19': xǁDASHStreamWorkerǁreload__mutmut_19, 
        'xǁDASHStreamWorkerǁreload__mutmut_20': xǁDASHStreamWorkerǁreload__mutmut_20, 
        'xǁDASHStreamWorkerǁreload__mutmut_21': xǁDASHStreamWorkerǁreload__mutmut_21, 
        'xǁDASHStreamWorkerǁreload__mutmut_22': xǁDASHStreamWorkerǁreload__mutmut_22, 
        'xǁDASHStreamWorkerǁreload__mutmut_23': xǁDASHStreamWorkerǁreload__mutmut_23, 
        'xǁDASHStreamWorkerǁreload__mutmut_24': xǁDASHStreamWorkerǁreload__mutmut_24, 
        'xǁDASHStreamWorkerǁreload__mutmut_25': xǁDASHStreamWorkerǁreload__mutmut_25, 
        'xǁDASHStreamWorkerǁreload__mutmut_26': xǁDASHStreamWorkerǁreload__mutmut_26, 
        'xǁDASHStreamWorkerǁreload__mutmut_27': xǁDASHStreamWorkerǁreload__mutmut_27, 
        'xǁDASHStreamWorkerǁreload__mutmut_28': xǁDASHStreamWorkerǁreload__mutmut_28, 
        'xǁDASHStreamWorkerǁreload__mutmut_29': xǁDASHStreamWorkerǁreload__mutmut_29, 
        'xǁDASHStreamWorkerǁreload__mutmut_30': xǁDASHStreamWorkerǁreload__mutmut_30
    }
    
    def reload(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamWorkerǁreload__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamWorkerǁreload__mutmut_mutants"), args, kwargs, self)
        return result 
    
    reload.__signature__ = _mutmut_signature(xǁDASHStreamWorkerǁreload__mutmut_orig)
    xǁDASHStreamWorkerǁreload__mutmut_orig.__name__ = 'xǁDASHStreamWorkerǁreload'


class DASHStreamReader(SegmentedStreamReader[DASHSegment, Response]):
    __worker__ = DASHStreamWorker
    __writer__ = DASHStreamWriter

    worker: DASHStreamWorker
    writer: DASHStreamWriter
    stream: DASHStream

    def xǁDASHStreamReaderǁ__init____mutmut_orig(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, name=name)
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_1(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(None, name=name)
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_2(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, name=None)
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_3(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(name=name)
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_4(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, )
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_5(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, name=name)
        self.ident = None
        self.mime_type = representation.mimeType
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_6(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, name=name)
        self.ident = representation.ident
        self.mime_type = None
        self.timestamp = timestamp

    def xǁDASHStreamReaderǁ__init____mutmut_7(
        self,
        stream: DASHStream,
        representation: Representation,
        timestamp: datetime,
        name: str | None = None,
    ):
        super().__init__(stream, name=name)
        self.ident = representation.ident
        self.mime_type = representation.mimeType
        self.timestamp = None
    
    xǁDASHStreamReaderǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamReaderǁ__init____mutmut_1': xǁDASHStreamReaderǁ__init____mutmut_1, 
        'xǁDASHStreamReaderǁ__init____mutmut_2': xǁDASHStreamReaderǁ__init____mutmut_2, 
        'xǁDASHStreamReaderǁ__init____mutmut_3': xǁDASHStreamReaderǁ__init____mutmut_3, 
        'xǁDASHStreamReaderǁ__init____mutmut_4': xǁDASHStreamReaderǁ__init____mutmut_4, 
        'xǁDASHStreamReaderǁ__init____mutmut_5': xǁDASHStreamReaderǁ__init____mutmut_5, 
        'xǁDASHStreamReaderǁ__init____mutmut_6': xǁDASHStreamReaderǁ__init____mutmut_6, 
        'xǁDASHStreamReaderǁ__init____mutmut_7': xǁDASHStreamReaderǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamReaderǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamReaderǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁDASHStreamReaderǁ__init____mutmut_orig)
    xǁDASHStreamReaderǁ__init____mutmut_orig.__name__ = 'xǁDASHStreamReaderǁ__init__'


class DASHStream(Stream):
    """
    Implementation of the "Dynamic Adaptive Streaming over HTTP" protocol (MPEG-DASH)
    """

    __shortname__ = "dash"

    def xǁDASHStreamǁ__init____mutmut_orig(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.mpd = mpd
        self.video_representation = video_representation
        self.audio_representation = audio_representation
        self.args = session.http.valid_request_args(**kwargs)

    def xǁDASHStreamǁ__init____mutmut_1(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(None)
        self.mpd = mpd
        self.video_representation = video_representation
        self.audio_representation = audio_representation
        self.args = session.http.valid_request_args(**kwargs)

    def xǁDASHStreamǁ__init____mutmut_2(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.mpd = None
        self.video_representation = video_representation
        self.audio_representation = audio_representation
        self.args = session.http.valid_request_args(**kwargs)

    def xǁDASHStreamǁ__init____mutmut_3(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.mpd = mpd
        self.video_representation = None
        self.audio_representation = audio_representation
        self.args = session.http.valid_request_args(**kwargs)

    def xǁDASHStreamǁ__init____mutmut_4(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.mpd = mpd
        self.video_representation = video_representation
        self.audio_representation = None
        self.args = session.http.valid_request_args(**kwargs)

    def xǁDASHStreamǁ__init____mutmut_5(
        self,
        session: Streamlink,
        mpd: MPD,
        video_representation: Representation | None = None,
        audio_representation: Representation | None = None,
        **kwargs,
    ):
        """
        :param session: Streamlink session instance
        :param mpd: Parsed MPD manifest
        :param video_representation: Video representation
        :param audio_representation: Audio representation
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        super().__init__(session)
        self.mpd = mpd
        self.video_representation = video_representation
        self.audio_representation = audio_representation
        self.args = None
    
    xǁDASHStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamǁ__init____mutmut_1': xǁDASHStreamǁ__init____mutmut_1, 
        'xǁDASHStreamǁ__init____mutmut_2': xǁDASHStreamǁ__init____mutmut_2, 
        'xǁDASHStreamǁ__init____mutmut_3': xǁDASHStreamǁ__init____mutmut_3, 
        'xǁDASHStreamǁ__init____mutmut_4': xǁDASHStreamǁ__init____mutmut_4, 
        'xǁDASHStreamǁ__init____mutmut_5': xǁDASHStreamǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁDASHStreamǁ__init____mutmut_orig)
    xǁDASHStreamǁ__init____mutmut_orig.__name__ = 'xǁDASHStreamǁ__init__'

    def xǁDASHStreamǁ__json____mutmut_orig(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_1(self):  # noqa: PLW3201
        json = None

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_2(self):  # noqa: PLW3201
        json = dict(typeXX=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_3(self):  # noqa: PLW3201
        json = dict(type=None)

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_4(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = None
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_5(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=None)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_6(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = None
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_7(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=None,
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_8(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=None,
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_9(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                headers=dict(req.headers),
            )

        return json

    def xǁDASHStreamǁ__json____mutmut_10(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                )

        return json

    def xǁDASHStreamǁ__json____mutmut_11(self):  # noqa: PLW3201
        json = dict(type=self.shortname())

        if self.mpd.url:
            args = self.args.copy()
            args.update(url=self.mpd.url)
            req = self.session.http.prepare_new_request(**args)
            json.update(
                # the MPD URL has already been prepared by the initial request in `parse_manifest`
                url=self.mpd.url,
                headers=dict(None),
            )

        return json
    
    xǁDASHStreamǁ__json____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamǁ__json____mutmut_1': xǁDASHStreamǁ__json____mutmut_1, 
        'xǁDASHStreamǁ__json____mutmut_2': xǁDASHStreamǁ__json____mutmut_2, 
        'xǁDASHStreamǁ__json____mutmut_3': xǁDASHStreamǁ__json____mutmut_3, 
        'xǁDASHStreamǁ__json____mutmut_4': xǁDASHStreamǁ__json____mutmut_4, 
        'xǁDASHStreamǁ__json____mutmut_5': xǁDASHStreamǁ__json____mutmut_5, 
        'xǁDASHStreamǁ__json____mutmut_6': xǁDASHStreamǁ__json____mutmut_6, 
        'xǁDASHStreamǁ__json____mutmut_7': xǁDASHStreamǁ__json____mutmut_7, 
        'xǁDASHStreamǁ__json____mutmut_8': xǁDASHStreamǁ__json____mutmut_8, 
        'xǁDASHStreamǁ__json____mutmut_9': xǁDASHStreamǁ__json____mutmut_9, 
        'xǁDASHStreamǁ__json____mutmut_10': xǁDASHStreamǁ__json____mutmut_10, 
        'xǁDASHStreamǁ__json____mutmut_11': xǁDASHStreamǁ__json____mutmut_11
    }
    
    def __json__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamǁ__json____mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamǁ__json____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __json__.__signature__ = _mutmut_signature(xǁDASHStreamǁ__json____mutmut_orig)
    xǁDASHStreamǁ__json____mutmut_orig.__name__ = 'xǁDASHStreamǁ__json__'

    def xǁDASHStreamǁto_url__mutmut_orig(self):
        if self.mpd.url is None:
            return super().to_url()

        # the MPD URL has already been prepared by the initial request in `parse_manifest`
        return self.mpd.url

    def xǁDASHStreamǁto_url__mutmut_1(self):
        if self.mpd.url is not None:
            return super().to_url()

        # the MPD URL has already been prepared by the initial request in `parse_manifest`
        return self.mpd.url
    
    xǁDASHStreamǁto_url__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamǁto_url__mutmut_1': xǁDASHStreamǁto_url__mutmut_1
    }
    
    def to_url(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamǁto_url__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamǁto_url__mutmut_mutants"), args, kwargs, self)
        return result 
    
    to_url.__signature__ = _mutmut_signature(xǁDASHStreamǁto_url__mutmut_orig)
    xǁDASHStreamǁto_url__mutmut_orig.__name__ = 'xǁDASHStreamǁto_url'

    @staticmethod
    def fetch_manifest(session: Streamlink, url_or_manifest: str, **request_args) -> tuple[str, dict[str, Any]]:
        if url_or_manifest.startswith("<?xml"):
            return url_or_manifest, {}

        retries = session.options.get("dash-manifest-reload-attempts")
        args = session.http.valid_request_args(**request_args)
        res = session.http.get(url_or_manifest, retries=retries, **args)
        manifest: str = res.text
        url: str = res.url

        return manifest, dict(url=url, base_url=url)

    @staticmethod
    def parse_mpd(manifest: str, mpd_params: Mapping[str, Any]) -> MPD:
        node = parse_xml(manifest, ignore_ns=True)

        return MPD(node, **mpd_params)

    @classmethod
    def parse_manifest(
        cls,
        session: Streamlink,
        url_or_manifest: str,
        period: int | str = 0,
        with_video_only: bool = False,
        with_audio_only: bool = False,
        **kwargs,
    ) -> dict[str, DASHStream]:
        """
        Parse a DASH manifest file and return its streams.

        :param session: Streamlink session instance
        :param url_or_manifest: URL of the manifest file or an XML manifest string
        :param period: Which MPD period to use (index number (int) or ``id`` attribute (str)) for finding representations
        :param with_video_only: Also return video-only streams, otherwise only return muxed streams
        :param with_audio_only: Also return audio-only streams, otherwise only return muxed streams
        :param kwargs: Additional keyword arguments passed to :meth:`requests.Session.request`
        """

        manifest, mpd_params = cls.fetch_manifest(session, url_or_manifest, **kwargs)

        try:
            mpd = cls.parse_mpd(manifest, mpd_params)
        except Exception as err:
            raise PluginError(f"Failed to parse MPD manifest: {err}") from err

        source = mpd_params.get("url", "MPD manifest")
        video: list[Representation | None] = [None] if with_audio_only else []
        audio: list[Representation | None] = [None] if with_video_only else []

        available_periods = [f"{idx}{f' (id={p.id!r})' if p.id is not None else ''}" for idx, p in enumerate(mpd.periods)]
        log.debug(f"Available DASH periods: {', '.join(available_periods)}")

        try:
            if isinstance(period, int):
                period_selection = mpd.periods[period]
            else:
                period_selection = mpd.periods_map[period]
        except LookupError:
            raise PluginError(
                f"DASH period {period!r} not found. Select a valid period by index or by id attribute value.",
            ) from None

        # Search for suitable video and audio representations
        for aset in period_selection.adaptationSets:
            if aset.contentProtections:
                raise PluginError(f"{source} is protected by DRM")
            for rep in aset.representations:
                if rep.contentProtections:
                    raise PluginError(f"{source} is protected by DRM")
                if rep.mimeType.startswith("video"):
                    video.append(rep)
                elif rep.mimeType.startswith("audio"):  # pragma: no branch
                    audio.append(rep)

        if not video:
            video.append(None)
        if not audio:
            audio.append(None)

        locale = session.localization
        locale_lang = locale.language
        lang = None
        available_languages = set()

        # if the locale is explicitly set, prefer that language over others
        for aud in audio:
            if aud and aud.lang:
                available_languages.add(aud.lang)
                with suppress(LookupError):
                    if locale.explicit and aud.lang and Language.get(aud.lang) == locale_lang:
                        lang = aud.lang

        if not lang:
            # filter by the first language that appears
            lang = audio[0].lang if audio[0] else None

        log.debug(
            f"Available languages for DASH audio streams: {', '.join(available_languages) or 'NONE'} (using: {lang or 'n/a'})",
        )

        # if the language is given by the stream, filter out other languages that do not match
        if len(available_languages) > 1:
            audio = [a for a in audio if a and (a.lang is None or a.lang == lang)]

        ret = []
        for vid, aud in itertools.product(video, audio):
            if not vid and not aud:
                continue

            stream = DASHStream(session, mpd, vid, aud, **kwargs)
            stream_name = []

            if vid:
                stream_name.append(f"{vid.height or vid.bandwidth_rounded:0.0f}{'p' if vid.height else 'k'}")
            if aud and len(audio) > 1:
                stream_name.append(f"a{aud.bandwidth:0.0f}k")
            ret.append(("+".join(stream_name), stream))

        # rename duplicate streams
        dict_value_list = defaultdict(list)
        for k, v in ret:
            dict_value_list[k].append(v)

        def sortby_bandwidth(dash_stream: DASHStream) -> float:
            if dash_stream.video_representation:
                return dash_stream.video_representation.bandwidth
            if dash_stream.audio_representation:
                return dash_stream.audio_representation.bandwidth
            return 0  # pragma: no cover

        ret_new = {}
        for q in dict_value_list:
            items = dict_value_list[q]

            with suppress(AttributeError):
                items = sorted(items, key=sortby_bandwidth, reverse=True)

            for n in range(len(items)):
                if n == 0:
                    ret_new[q] = items[n]
                elif n == 1:
                    ret_new[f"{q}_alt"] = items[n]
                else:
                    ret_new[f"{q}_alt{n}"] = items[n]

        return ret_new

    def xǁDASHStreamǁopen__mutmut_orig(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_1(self):
        video, audio = None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_2(self):
        video, audio = None, None
        rep_video, rep_audio = None

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_3(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = None

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_4(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = None
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_5(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(None, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_6(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, None, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_7(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, None, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_8(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name=None)
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_9(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_10(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_11(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_12(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, )
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_13(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="XXvideoXX")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_14(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="VIDEO")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_15(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="Video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_16(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(None)

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_17(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = None
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_18(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(None, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_19(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, None, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_20(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, None, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_21(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name=None)
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_22(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_23(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_24(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_25(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, )
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_26(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="XXaudioXX")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_27(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="AUDIO")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_28(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="Audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_29(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(None)

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_30(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video or audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_31(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio or FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_32(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(None):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_33(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(None, video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_34(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, None, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_35(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, None, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_36(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=None).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_37(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(video, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_38(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, audio, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_39(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, copyts=True).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_40(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, ).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio

    def xǁDASHStreamǁopen__mutmut_41(self):
        video, audio = None, None
        rep_video, rep_audio = self.video_representation, self.audio_representation

        timestamp = now()

        if rep_video:
            video = DASHStreamReader(self, rep_video, timestamp, name="video")
            log.debug(f"Opening DASH reader for: {rep_video.ident!r} - {rep_video.mimeType}")

        if rep_audio:
            audio = DASHStreamReader(self, rep_audio, timestamp, name="audio")
            log.debug(f"Opening DASH reader for: {rep_audio.ident!r} - {rep_audio.mimeType}")

        if video and audio and FFMPEGMuxer.is_usable(self.session):
            video.open()
            audio.open()
            return FFMPEGMuxer(self.session, video, audio, copyts=False).open()
        elif video:
            video.open()
            return video
        elif audio:
            audio.open()
            return audio
    
    xǁDASHStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁDASHStreamǁopen__mutmut_1': xǁDASHStreamǁopen__mutmut_1, 
        'xǁDASHStreamǁopen__mutmut_2': xǁDASHStreamǁopen__mutmut_2, 
        'xǁDASHStreamǁopen__mutmut_3': xǁDASHStreamǁopen__mutmut_3, 
        'xǁDASHStreamǁopen__mutmut_4': xǁDASHStreamǁopen__mutmut_4, 
        'xǁDASHStreamǁopen__mutmut_5': xǁDASHStreamǁopen__mutmut_5, 
        'xǁDASHStreamǁopen__mutmut_6': xǁDASHStreamǁopen__mutmut_6, 
        'xǁDASHStreamǁopen__mutmut_7': xǁDASHStreamǁopen__mutmut_7, 
        'xǁDASHStreamǁopen__mutmut_8': xǁDASHStreamǁopen__mutmut_8, 
        'xǁDASHStreamǁopen__mutmut_9': xǁDASHStreamǁopen__mutmut_9, 
        'xǁDASHStreamǁopen__mutmut_10': xǁDASHStreamǁopen__mutmut_10, 
        'xǁDASHStreamǁopen__mutmut_11': xǁDASHStreamǁopen__mutmut_11, 
        'xǁDASHStreamǁopen__mutmut_12': xǁDASHStreamǁopen__mutmut_12, 
        'xǁDASHStreamǁopen__mutmut_13': xǁDASHStreamǁopen__mutmut_13, 
        'xǁDASHStreamǁopen__mutmut_14': xǁDASHStreamǁopen__mutmut_14, 
        'xǁDASHStreamǁopen__mutmut_15': xǁDASHStreamǁopen__mutmut_15, 
        'xǁDASHStreamǁopen__mutmut_16': xǁDASHStreamǁopen__mutmut_16, 
        'xǁDASHStreamǁopen__mutmut_17': xǁDASHStreamǁopen__mutmut_17, 
        'xǁDASHStreamǁopen__mutmut_18': xǁDASHStreamǁopen__mutmut_18, 
        'xǁDASHStreamǁopen__mutmut_19': xǁDASHStreamǁopen__mutmut_19, 
        'xǁDASHStreamǁopen__mutmut_20': xǁDASHStreamǁopen__mutmut_20, 
        'xǁDASHStreamǁopen__mutmut_21': xǁDASHStreamǁopen__mutmut_21, 
        'xǁDASHStreamǁopen__mutmut_22': xǁDASHStreamǁopen__mutmut_22, 
        'xǁDASHStreamǁopen__mutmut_23': xǁDASHStreamǁopen__mutmut_23, 
        'xǁDASHStreamǁopen__mutmut_24': xǁDASHStreamǁopen__mutmut_24, 
        'xǁDASHStreamǁopen__mutmut_25': xǁDASHStreamǁopen__mutmut_25, 
        'xǁDASHStreamǁopen__mutmut_26': xǁDASHStreamǁopen__mutmut_26, 
        'xǁDASHStreamǁopen__mutmut_27': xǁDASHStreamǁopen__mutmut_27, 
        'xǁDASHStreamǁopen__mutmut_28': xǁDASHStreamǁopen__mutmut_28, 
        'xǁDASHStreamǁopen__mutmut_29': xǁDASHStreamǁopen__mutmut_29, 
        'xǁDASHStreamǁopen__mutmut_30': xǁDASHStreamǁopen__mutmut_30, 
        'xǁDASHStreamǁopen__mutmut_31': xǁDASHStreamǁopen__mutmut_31, 
        'xǁDASHStreamǁopen__mutmut_32': xǁDASHStreamǁopen__mutmut_32, 
        'xǁDASHStreamǁopen__mutmut_33': xǁDASHStreamǁopen__mutmut_33, 
        'xǁDASHStreamǁopen__mutmut_34': xǁDASHStreamǁopen__mutmut_34, 
        'xǁDASHStreamǁopen__mutmut_35': xǁDASHStreamǁopen__mutmut_35, 
        'xǁDASHStreamǁopen__mutmut_36': xǁDASHStreamǁopen__mutmut_36, 
        'xǁDASHStreamǁopen__mutmut_37': xǁDASHStreamǁopen__mutmut_37, 
        'xǁDASHStreamǁopen__mutmut_38': xǁDASHStreamǁopen__mutmut_38, 
        'xǁDASHStreamǁopen__mutmut_39': xǁDASHStreamǁopen__mutmut_39, 
        'xǁDASHStreamǁopen__mutmut_40': xǁDASHStreamǁopen__mutmut_40, 
        'xǁDASHStreamǁopen__mutmut_41': xǁDASHStreamǁopen__mutmut_41
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁDASHStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁDASHStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁDASHStreamǁopen__mutmut_orig)
    xǁDASHStreamǁopen__mutmut_orig.__name__ = 'xǁDASHStreamǁopen'

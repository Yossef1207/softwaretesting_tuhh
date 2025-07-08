from __future__ import annotations

import concurrent.futures
import logging
import re
import subprocess
import sys
import threading
from collections.abc import Sequence
from contextlib import suppress
from functools import lru_cache
from pathlib import Path
from shutil import which
from typing import Any, ClassVar, Generic, TextIO, TypeVar

from streamlink import StreamError
from streamlink.stream.stream import Stream, StreamIO
from streamlink.utils.named_pipe import NamedPipe, NamedPipeBase
from streamlink.utils.processoutput import ProcessOutput


log = logging.getLogger(__name__)

_lock_resolve_command = threading.Lock()


TSubstreams_co = TypeVar("TSubstreams_co", bound=Stream, covariant=True)
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


class MuxedStream(Stream, Generic[TSubstreams_co]):
    """
    Muxes multiple streams into one output stream.
    """

    __shortname__ = "muxed-stream"

    def xǁMuxedStreamǁ__init____mutmut_orig(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("subtitles", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_1(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(None)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("subtitles", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_2(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = None
        self.subtitles: dict[str, Stream] = options.pop("subtitles", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_3(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = None
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_4(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop(None, {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_5(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("subtitles", None)
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_6(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop({})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_7(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("subtitles", )
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_8(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("XXsubtitlesXX", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_9(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("SUBTITLES", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_10(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("Subtitles", {})
        self.options: dict[str, Any] = options

    def xǁMuxedStreamǁ__init____mutmut_11(
        self,
        session,
        *substreams: TSubstreams_co,
        **options,
    ):
        """
        :param streamlink.Streamlink session: Streamlink session instance
        :param substreams: Video and/or audio streams
        :param options: Additional keyword arguments passed to :class:`ffmpegmux.FFMPEGMuxer`.
                        Subtitle streams need to be set via the ``subtitles`` keyword.
        """

        super().__init__(session)
        self.substreams: Sequence[TSubstreams_co] = substreams
        self.subtitles: dict[str, Stream] = options.pop("subtitles", {})
        self.options: dict[str, Any] = None
    
    xǁMuxedStreamǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMuxedStreamǁ__init____mutmut_1': xǁMuxedStreamǁ__init____mutmut_1, 
        'xǁMuxedStreamǁ__init____mutmut_2': xǁMuxedStreamǁ__init____mutmut_2, 
        'xǁMuxedStreamǁ__init____mutmut_3': xǁMuxedStreamǁ__init____mutmut_3, 
        'xǁMuxedStreamǁ__init____mutmut_4': xǁMuxedStreamǁ__init____mutmut_4, 
        'xǁMuxedStreamǁ__init____mutmut_5': xǁMuxedStreamǁ__init____mutmut_5, 
        'xǁMuxedStreamǁ__init____mutmut_6': xǁMuxedStreamǁ__init____mutmut_6, 
        'xǁMuxedStreamǁ__init____mutmut_7': xǁMuxedStreamǁ__init____mutmut_7, 
        'xǁMuxedStreamǁ__init____mutmut_8': xǁMuxedStreamǁ__init____mutmut_8, 
        'xǁMuxedStreamǁ__init____mutmut_9': xǁMuxedStreamǁ__init____mutmut_9, 
        'xǁMuxedStreamǁ__init____mutmut_10': xǁMuxedStreamǁ__init____mutmut_10, 
        'xǁMuxedStreamǁ__init____mutmut_11': xǁMuxedStreamǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMuxedStreamǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁMuxedStreamǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁMuxedStreamǁ__init____mutmut_orig)
    xǁMuxedStreamǁ__init____mutmut_orig.__name__ = 'xǁMuxedStreamǁ__init__'

    def xǁMuxedStreamǁopen__mutmut_orig(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_1(self):
        fds = None
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_2(self):
        fds = []
        metadata = None
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_3(self):
        fds = []
        metadata = self.options.get(None, {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_4(self):
        fds = []
        metadata = self.options.get("metadata", None)
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_5(self):
        fds = []
        metadata = self.options.get({})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_6(self):
        fds = []
        metadata = self.options.get("metadata", )
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_7(self):
        fds = []
        metadata = self.options.get("XXmetadataXX", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_8(self):
        fds = []
        metadata = self.options.get("METADATA", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_9(self):
        fds = []
        metadata = self.options.get("Metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_10(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = None
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_11(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get(None, [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_12(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", None)
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_13(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get([])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_14(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", )
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_15(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("XXmapsXX", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_16(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("MAPS", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_17(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("Maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_18(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = None
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_19(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_20(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug(None)
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_21(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(None))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_22(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("XXOpening {0} substreamXX".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_23(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_24(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("OPENING {0} SUBSTREAM".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_25(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(None)
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_26(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(None)

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_27(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream or substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_28(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(None):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_29(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = None
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_30(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug(None)
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_31(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(None))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_32(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("XXOpening {0} subtitle streamXX".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_33(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_34(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("OPENING {0} SUBTITLE STREAM".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_35(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(None)
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_36(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(None)
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_37(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream or substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_38(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = None

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_39(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(None)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_40(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["XXs:s:{0}XX".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_41(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["S:S:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_42(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["S:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_43(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(None)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_44(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["XXlanguage={0}XX".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_45(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["LANGUAGE={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_46(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["Language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_47(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = None
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_48(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["XXmetadataXX"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_49(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["METADATA"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_50(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["Metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_51(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = None

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_52(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["XXmapsXX"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_53(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["MAPS"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_54(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["Maps"] = maps

        return FFMPEGMuxer(self.session, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_55(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(None, *fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_56(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(*fds, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_57(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, **self.options).open()

    def xǁMuxedStreamǁopen__mutmut_58(self):
        fds = []
        metadata = self.options.get("metadata", {})
        maps = self.options.get("maps", [])
        # only update the maps values if they haven't been set
        update_maps = not maps
        for substream in self.substreams:
            log.debug("Opening {0} substream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())

        for i, subtitle in enumerate(self.subtitles.items()):
            language, substream = subtitle
            log.debug("Opening {0} subtitle stream".format(substream.shortname()))
            if update_maps:
                maps.append(len(fds))
            fds.append(substream and substream.open())
            metadata["s:s:{0}".format(i)] = ["language={0}".format(language)]

        self.options["metadata"] = metadata
        self.options["maps"] = maps

        return FFMPEGMuxer(self.session, *fds, ).open()
    
    xǁMuxedStreamǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁMuxedStreamǁopen__mutmut_1': xǁMuxedStreamǁopen__mutmut_1, 
        'xǁMuxedStreamǁopen__mutmut_2': xǁMuxedStreamǁopen__mutmut_2, 
        'xǁMuxedStreamǁopen__mutmut_3': xǁMuxedStreamǁopen__mutmut_3, 
        'xǁMuxedStreamǁopen__mutmut_4': xǁMuxedStreamǁopen__mutmut_4, 
        'xǁMuxedStreamǁopen__mutmut_5': xǁMuxedStreamǁopen__mutmut_5, 
        'xǁMuxedStreamǁopen__mutmut_6': xǁMuxedStreamǁopen__mutmut_6, 
        'xǁMuxedStreamǁopen__mutmut_7': xǁMuxedStreamǁopen__mutmut_7, 
        'xǁMuxedStreamǁopen__mutmut_8': xǁMuxedStreamǁopen__mutmut_8, 
        'xǁMuxedStreamǁopen__mutmut_9': xǁMuxedStreamǁopen__mutmut_9, 
        'xǁMuxedStreamǁopen__mutmut_10': xǁMuxedStreamǁopen__mutmut_10, 
        'xǁMuxedStreamǁopen__mutmut_11': xǁMuxedStreamǁopen__mutmut_11, 
        'xǁMuxedStreamǁopen__mutmut_12': xǁMuxedStreamǁopen__mutmut_12, 
        'xǁMuxedStreamǁopen__mutmut_13': xǁMuxedStreamǁopen__mutmut_13, 
        'xǁMuxedStreamǁopen__mutmut_14': xǁMuxedStreamǁopen__mutmut_14, 
        'xǁMuxedStreamǁopen__mutmut_15': xǁMuxedStreamǁopen__mutmut_15, 
        'xǁMuxedStreamǁopen__mutmut_16': xǁMuxedStreamǁopen__mutmut_16, 
        'xǁMuxedStreamǁopen__mutmut_17': xǁMuxedStreamǁopen__mutmut_17, 
        'xǁMuxedStreamǁopen__mutmut_18': xǁMuxedStreamǁopen__mutmut_18, 
        'xǁMuxedStreamǁopen__mutmut_19': xǁMuxedStreamǁopen__mutmut_19, 
        'xǁMuxedStreamǁopen__mutmut_20': xǁMuxedStreamǁopen__mutmut_20, 
        'xǁMuxedStreamǁopen__mutmut_21': xǁMuxedStreamǁopen__mutmut_21, 
        'xǁMuxedStreamǁopen__mutmut_22': xǁMuxedStreamǁopen__mutmut_22, 
        'xǁMuxedStreamǁopen__mutmut_23': xǁMuxedStreamǁopen__mutmut_23, 
        'xǁMuxedStreamǁopen__mutmut_24': xǁMuxedStreamǁopen__mutmut_24, 
        'xǁMuxedStreamǁopen__mutmut_25': xǁMuxedStreamǁopen__mutmut_25, 
        'xǁMuxedStreamǁopen__mutmut_26': xǁMuxedStreamǁopen__mutmut_26, 
        'xǁMuxedStreamǁopen__mutmut_27': xǁMuxedStreamǁopen__mutmut_27, 
        'xǁMuxedStreamǁopen__mutmut_28': xǁMuxedStreamǁopen__mutmut_28, 
        'xǁMuxedStreamǁopen__mutmut_29': xǁMuxedStreamǁopen__mutmut_29, 
        'xǁMuxedStreamǁopen__mutmut_30': xǁMuxedStreamǁopen__mutmut_30, 
        'xǁMuxedStreamǁopen__mutmut_31': xǁMuxedStreamǁopen__mutmut_31, 
        'xǁMuxedStreamǁopen__mutmut_32': xǁMuxedStreamǁopen__mutmut_32, 
        'xǁMuxedStreamǁopen__mutmut_33': xǁMuxedStreamǁopen__mutmut_33, 
        'xǁMuxedStreamǁopen__mutmut_34': xǁMuxedStreamǁopen__mutmut_34, 
        'xǁMuxedStreamǁopen__mutmut_35': xǁMuxedStreamǁopen__mutmut_35, 
        'xǁMuxedStreamǁopen__mutmut_36': xǁMuxedStreamǁopen__mutmut_36, 
        'xǁMuxedStreamǁopen__mutmut_37': xǁMuxedStreamǁopen__mutmut_37, 
        'xǁMuxedStreamǁopen__mutmut_38': xǁMuxedStreamǁopen__mutmut_38, 
        'xǁMuxedStreamǁopen__mutmut_39': xǁMuxedStreamǁopen__mutmut_39, 
        'xǁMuxedStreamǁopen__mutmut_40': xǁMuxedStreamǁopen__mutmut_40, 
        'xǁMuxedStreamǁopen__mutmut_41': xǁMuxedStreamǁopen__mutmut_41, 
        'xǁMuxedStreamǁopen__mutmut_42': xǁMuxedStreamǁopen__mutmut_42, 
        'xǁMuxedStreamǁopen__mutmut_43': xǁMuxedStreamǁopen__mutmut_43, 
        'xǁMuxedStreamǁopen__mutmut_44': xǁMuxedStreamǁopen__mutmut_44, 
        'xǁMuxedStreamǁopen__mutmut_45': xǁMuxedStreamǁopen__mutmut_45, 
        'xǁMuxedStreamǁopen__mutmut_46': xǁMuxedStreamǁopen__mutmut_46, 
        'xǁMuxedStreamǁopen__mutmut_47': xǁMuxedStreamǁopen__mutmut_47, 
        'xǁMuxedStreamǁopen__mutmut_48': xǁMuxedStreamǁopen__mutmut_48, 
        'xǁMuxedStreamǁopen__mutmut_49': xǁMuxedStreamǁopen__mutmut_49, 
        'xǁMuxedStreamǁopen__mutmut_50': xǁMuxedStreamǁopen__mutmut_50, 
        'xǁMuxedStreamǁopen__mutmut_51': xǁMuxedStreamǁopen__mutmut_51, 
        'xǁMuxedStreamǁopen__mutmut_52': xǁMuxedStreamǁopen__mutmut_52, 
        'xǁMuxedStreamǁopen__mutmut_53': xǁMuxedStreamǁopen__mutmut_53, 
        'xǁMuxedStreamǁopen__mutmut_54': xǁMuxedStreamǁopen__mutmut_54, 
        'xǁMuxedStreamǁopen__mutmut_55': xǁMuxedStreamǁopen__mutmut_55, 
        'xǁMuxedStreamǁopen__mutmut_56': xǁMuxedStreamǁopen__mutmut_56, 
        'xǁMuxedStreamǁopen__mutmut_57': xǁMuxedStreamǁopen__mutmut_57, 
        'xǁMuxedStreamǁopen__mutmut_58': xǁMuxedStreamǁopen__mutmut_58
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁMuxedStreamǁopen__mutmut_orig"), object.__getattribute__(self, "xǁMuxedStreamǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁMuxedStreamǁopen__mutmut_orig)
    xǁMuxedStreamǁopen__mutmut_orig.__name__ = 'xǁMuxedStreamǁopen'

    @classmethod
    def is_usable(cls, session):
        return FFMPEGMuxer.is_usable(session)


class FFMPEGMuxer(StreamIO):
    __commands__: ClassVar[list[str]] = ["ffmpeg"]

    DEFAULT_LOGLEVEL = "info"
    DEFAULT_OUTPUT_FORMAT = "matroska"
    DEFAULT_VIDEO_CODEC = "copy"
    DEFAULT_AUDIO_CODEC = "copy"

    FFMPEG_VERSION: str | None = None
    FFMPEG_VERSION_TIMEOUT = 4.0

    errorlog: int | TextIO

    process: subprocess.Popen | None

    @classmethod
    def is_usable(cls, session):
        return cls.command(session) is not None

    @classmethod
    def command(cls, session):
        with _lock_resolve_command:
            return cls._resolve_command(
                session.options.get("ffmpeg-ffmpeg"),
                not session.options.get("ffmpeg-no-validation"),
            )

    @classmethod
    @lru_cache(maxsize=128)
    def _resolve_command(cls, command: str | None = None, validate: bool = True) -> str | None:
        if command:
            resolved = which(command)
        else:
            resolved = None
            for cmd in cls.__commands__:
                resolved = which(cmd)
                if resolved:
                    break

        if resolved and validate:
            log.trace(f"Querying FFmpeg version: {[resolved, '-version']}")  # type: ignore[attr-defined]
            versionoutput = FFmpegVersionOutput([resolved, "-version"], timeout=cls.FFMPEG_VERSION_TIMEOUT)
            if not versionoutput.run():
                log.error("Could not validate FFmpeg!")
                log.error(f"Unexpected FFmpeg version output while running {[resolved, '-version']}")
                resolved = None
            else:
                cls.FFMPEG_VERSION = versionoutput.version
                for i, line in enumerate(versionoutput.output):
                    log.debug(f" {line}" if i > 0 else line)

        if not resolved:
            log.warning("No valid FFmpeg binary was found. See the --ffmpeg-ffmpeg option.")
            log.warning("Muxing streams is unsupported! Only a subset of the available streams can be returned!")

        return resolved

    @staticmethod
    def copy_to_pipe(muxer: FFMPEGMuxer, stream: StreamIO, pipe: NamedPipeBase):
        log.debug(f"Starting copy to pipe: {pipe.path}")
        # TODO: catch OSError when creating/opening pipe fails and close entire output stream
        pipe.open()

        data = b""
        while True:
            try:
                data = stream.read(8192)
            except (OSError, ValueError) as err:
                log.error(f"Error while reading from substream: {err}")
                break

            if data == b"":
                log.debug(f"Pipe copy complete: {pipe.path}")
                break

            try:
                pipe.write(data)
            except OSError as err:
                if stream.closed or not muxer.process or not muxer.process.poll():
                    log.debug(f"Pipe copy complete: {pipe.path}")
                    break
                log.error(f"Error while writing to pipe {pipe.path}: {err}")
                break

        with suppress(OSError):
            pipe.close()

    def xǁFFMPEGMuxerǁ__init____mutmut_orig(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_1(self, session, *streams, **options):
        self.session = None
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_2(self, session, *streams, **options):
        self.session = session
        self.process = ""
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_3(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = None

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_4(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_5(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(None):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_6(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError(None)

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_7(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("XXCannot use FFmpegXX")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_8(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("cannot use ffmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_9(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("CANNOT USE FFMPEG")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_10(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use ffmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_11(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = None
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_12(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = None
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_13(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = None

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_14(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=None,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_15(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=None,
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_16(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_17(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_18(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(None, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_19(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, None)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_20(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_21(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, )
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_22(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = None
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_23(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get(None) or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_24(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("XXffmpeg-loglevelXX") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_25(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("FFMPEG-LOGLEVEL") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_26(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("Ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_27(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") and options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_28(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop(None, self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_29(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", None)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_30(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop(self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_31(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", )
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_32(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("XXloglevelXX", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_33(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("LOGLEVEL", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_34(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("Loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_35(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = None
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_36(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get(None) or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_37(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("XXffmpeg-foutXX") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_38(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("FFMPEG-FOUT") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_39(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("Ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_40(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") and options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_41(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop(None, self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_42(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", None)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_43(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop(self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_44(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", )
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_45(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("XXformatXX", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_46(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("FORMAT", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_47(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("Format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_48(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = None
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_49(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop(None, "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_50(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", None)
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_51(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_52(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", )
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_53(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("XXoutpathXX", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_54(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("OUTPATH", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_55(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("Outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_56(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "XXpipe:1XX")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_57(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "PIPE:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_58(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "Pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_59(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = None
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_60(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get(None) or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_61(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("XXffmpeg-video-transcodeXX") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_62(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("FFMPEG-VIDEO-TRANSCODE") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_63(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("Ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_64(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") and options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_65(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop(None, self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_66(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", None)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_67(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop(self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_68(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", )
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_69(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("XXvcodecXX", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_70(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("VCODEC", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_71(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("Vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_72(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = None
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_73(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get(None) or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_74(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("XXffmpeg-audio-transcodeXX") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_75(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("FFMPEG-AUDIO-TRANSCODE") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_76(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("Ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_77(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") and options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_78(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop(None, self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_79(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", None)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_80(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop(self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_81(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", )
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_82(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("XXacodecXX", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_83(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("ACODEC", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_84(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("Acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_85(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = None
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_86(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop(None, {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_87(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", None)
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_88(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop({})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_89(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", )
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_90(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("XXmetadataXX", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_91(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("METADATA", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_92(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("Metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_93(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = None
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_94(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop(None, [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_95(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", None)
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_96(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop([])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_97(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", )
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_98(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("XXmapsXX", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_99(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("MAPS", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_100(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("Maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_101(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = None
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_102(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get(None) or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_103(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("XXffmpeg-copytsXX") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_104(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("FFMPEG-COPYTS") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_105(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("Ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_106(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") and options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_107(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop(None, False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_108(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", None)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_109(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop(False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_110(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", )
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_111(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("XXcopytsXX", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_112(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("COPYTS", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_113(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("Copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_114(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", True)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_115(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = None

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_116(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get(None) or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_117(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("XXffmpeg-start-at-zeroXX") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_118(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("FFMPEG-START-AT-ZERO") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_119(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("Ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_120(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") and options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_121(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop(None, False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_122(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", None)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_123(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop(False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_124(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", )

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_125(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("XXstart_at_zeroXX", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_126(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("START_AT_ZERO", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_127(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("Start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_128(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", True)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_129(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = None

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_130(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(None),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_131(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "XX-yXX",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_132(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-Y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_133(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "XX-nostatsXX",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_134(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-NOSTATS",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_135(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "XX-loglevelXX",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_136(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-LOGLEVEL",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_137(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(None)

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_138(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["XX-iXX", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_139(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-I", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_140(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(None)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_141(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(None)
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_142(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["XX-c:vXX", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_143(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-C:V", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_144(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(None)

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_145(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["XX-c:aXX", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_146(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-C:A", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_147(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(None)

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_148(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["XX-mapXX", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_149(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-MAP", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_150(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(None)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_151(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(None)
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_152(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["XX-copytsXX"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_153(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-COPYTS"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_154(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(None)

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_155(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["XX-start_at_zeroXX"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_156(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-START_AT_ZERO"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_157(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = None
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_158(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(None) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_159(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = "XX:{0}XX".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_160(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else "XXXX"
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_161(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(None)

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_162(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(None), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_163(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["XX-metadata{0}XX".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_164(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-METADATA{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_165(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(None)
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_166(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["XX-fXX", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_167(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-F", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_168(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(None)

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_169(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get(None):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_170(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("XXffmpeg-verbose-pathXX"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_171(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("FFMPEG-VERBOSE-PATH"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_172(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("Ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_173(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = None
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_174(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open(None)
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_175(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(None).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_176(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get(None)).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_177(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("XXffmpeg-verbose-pathXX")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_178(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("FFMPEG-VERBOSE-PATH")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_179(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("Ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_180(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("XXwXX")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_181(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("W")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_182(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("W")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_183(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get(None):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_184(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("XXffmpeg-verboseXX"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_185(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("FFMPEG-VERBOSE"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_186(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("Ffmpeg-verbose"):
            self.errorlog = sys.stderr

    def xǁFFMPEGMuxerǁ__init____mutmut_187(self, session, *streams, **options):
        self.session = session
        self.process = None
        self.errorlog = subprocess.DEVNULL

        if not self.is_usable(session):
            raise StreamError("Cannot use FFmpeg")

        self.streams = streams
        self.pipes = [NamedPipe() for _ in self.streams]
        self.pipe_threads = [
            threading.Thread(
                target=self.copy_to_pipe,
                args=(self, stream, np),
            )
            for stream, np in zip(self.streams, self.pipes)
        ]

        loglevel = session.options.get("ffmpeg-loglevel") or options.pop("loglevel", self.DEFAULT_LOGLEVEL)
        ofmt = session.options.get("ffmpeg-fout") or options.pop("format", self.DEFAULT_OUTPUT_FORMAT)
        outpath = options.pop("outpath", "pipe:1")
        videocodec = session.options.get("ffmpeg-video-transcode") or options.pop("vcodec", self.DEFAULT_VIDEO_CODEC)
        audiocodec = session.options.get("ffmpeg-audio-transcode") or options.pop("acodec", self.DEFAULT_AUDIO_CODEC)
        metadata = options.pop("metadata", {})
        maps = options.pop("maps", [])
        copyts = session.options.get("ffmpeg-copyts") or options.pop("copyts", False)
        start_at_zero = session.options.get("ffmpeg-start-at-zero") or options.pop("start_at_zero", False)

        self._cmd = [
            self.command(session),
            "-y",
            "-nostats",
            "-loglevel",
            loglevel,
        ]

        for np in self.pipes:
            self._cmd.extend(["-i", str(np.path)])

        self._cmd.extend(["-c:v", videocodec])
        self._cmd.extend(["-c:a", audiocodec])

        for m in maps:
            self._cmd.extend(["-map", str(m)])

        if copyts:
            self._cmd.extend(["-copyts"])
            if start_at_zero:
                self._cmd.extend(["-start_at_zero"])

        for stream, data in metadata.items():
            for datum in data:
                stream_id = ":{0}".format(stream) if stream else ""
                self._cmd.extend(["-metadata{0}".format(stream_id), datum])

        self._cmd.extend(["-f", ofmt, outpath])
        log.debug(f"ffmpeg command: {self._cmd!r}")

        if session.options.get("ffmpeg-verbose-path"):
            self.errorlog = Path(session.options.get("ffmpeg-verbose-path")).expanduser().open("w")
        elif session.options.get("ffmpeg-verbose"):
            self.errorlog = None
    
    xǁFFMPEGMuxerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFMPEGMuxerǁ__init____mutmut_1': xǁFFMPEGMuxerǁ__init____mutmut_1, 
        'xǁFFMPEGMuxerǁ__init____mutmut_2': xǁFFMPEGMuxerǁ__init____mutmut_2, 
        'xǁFFMPEGMuxerǁ__init____mutmut_3': xǁFFMPEGMuxerǁ__init____mutmut_3, 
        'xǁFFMPEGMuxerǁ__init____mutmut_4': xǁFFMPEGMuxerǁ__init____mutmut_4, 
        'xǁFFMPEGMuxerǁ__init____mutmut_5': xǁFFMPEGMuxerǁ__init____mutmut_5, 
        'xǁFFMPEGMuxerǁ__init____mutmut_6': xǁFFMPEGMuxerǁ__init____mutmut_6, 
        'xǁFFMPEGMuxerǁ__init____mutmut_7': xǁFFMPEGMuxerǁ__init____mutmut_7, 
        'xǁFFMPEGMuxerǁ__init____mutmut_8': xǁFFMPEGMuxerǁ__init____mutmut_8, 
        'xǁFFMPEGMuxerǁ__init____mutmut_9': xǁFFMPEGMuxerǁ__init____mutmut_9, 
        'xǁFFMPEGMuxerǁ__init____mutmut_10': xǁFFMPEGMuxerǁ__init____mutmut_10, 
        'xǁFFMPEGMuxerǁ__init____mutmut_11': xǁFFMPEGMuxerǁ__init____mutmut_11, 
        'xǁFFMPEGMuxerǁ__init____mutmut_12': xǁFFMPEGMuxerǁ__init____mutmut_12, 
        'xǁFFMPEGMuxerǁ__init____mutmut_13': xǁFFMPEGMuxerǁ__init____mutmut_13, 
        'xǁFFMPEGMuxerǁ__init____mutmut_14': xǁFFMPEGMuxerǁ__init____mutmut_14, 
        'xǁFFMPEGMuxerǁ__init____mutmut_15': xǁFFMPEGMuxerǁ__init____mutmut_15, 
        'xǁFFMPEGMuxerǁ__init____mutmut_16': xǁFFMPEGMuxerǁ__init____mutmut_16, 
        'xǁFFMPEGMuxerǁ__init____mutmut_17': xǁFFMPEGMuxerǁ__init____mutmut_17, 
        'xǁFFMPEGMuxerǁ__init____mutmut_18': xǁFFMPEGMuxerǁ__init____mutmut_18, 
        'xǁFFMPEGMuxerǁ__init____mutmut_19': xǁFFMPEGMuxerǁ__init____mutmut_19, 
        'xǁFFMPEGMuxerǁ__init____mutmut_20': xǁFFMPEGMuxerǁ__init____mutmut_20, 
        'xǁFFMPEGMuxerǁ__init____mutmut_21': xǁFFMPEGMuxerǁ__init____mutmut_21, 
        'xǁFFMPEGMuxerǁ__init____mutmut_22': xǁFFMPEGMuxerǁ__init____mutmut_22, 
        'xǁFFMPEGMuxerǁ__init____mutmut_23': xǁFFMPEGMuxerǁ__init____mutmut_23, 
        'xǁFFMPEGMuxerǁ__init____mutmut_24': xǁFFMPEGMuxerǁ__init____mutmut_24, 
        'xǁFFMPEGMuxerǁ__init____mutmut_25': xǁFFMPEGMuxerǁ__init____mutmut_25, 
        'xǁFFMPEGMuxerǁ__init____mutmut_26': xǁFFMPEGMuxerǁ__init____mutmut_26, 
        'xǁFFMPEGMuxerǁ__init____mutmut_27': xǁFFMPEGMuxerǁ__init____mutmut_27, 
        'xǁFFMPEGMuxerǁ__init____mutmut_28': xǁFFMPEGMuxerǁ__init____mutmut_28, 
        'xǁFFMPEGMuxerǁ__init____mutmut_29': xǁFFMPEGMuxerǁ__init____mutmut_29, 
        'xǁFFMPEGMuxerǁ__init____mutmut_30': xǁFFMPEGMuxerǁ__init____mutmut_30, 
        'xǁFFMPEGMuxerǁ__init____mutmut_31': xǁFFMPEGMuxerǁ__init____mutmut_31, 
        'xǁFFMPEGMuxerǁ__init____mutmut_32': xǁFFMPEGMuxerǁ__init____mutmut_32, 
        'xǁFFMPEGMuxerǁ__init____mutmut_33': xǁFFMPEGMuxerǁ__init____mutmut_33, 
        'xǁFFMPEGMuxerǁ__init____mutmut_34': xǁFFMPEGMuxerǁ__init____mutmut_34, 
        'xǁFFMPEGMuxerǁ__init____mutmut_35': xǁFFMPEGMuxerǁ__init____mutmut_35, 
        'xǁFFMPEGMuxerǁ__init____mutmut_36': xǁFFMPEGMuxerǁ__init____mutmut_36, 
        'xǁFFMPEGMuxerǁ__init____mutmut_37': xǁFFMPEGMuxerǁ__init____mutmut_37, 
        'xǁFFMPEGMuxerǁ__init____mutmut_38': xǁFFMPEGMuxerǁ__init____mutmut_38, 
        'xǁFFMPEGMuxerǁ__init____mutmut_39': xǁFFMPEGMuxerǁ__init____mutmut_39, 
        'xǁFFMPEGMuxerǁ__init____mutmut_40': xǁFFMPEGMuxerǁ__init____mutmut_40, 
        'xǁFFMPEGMuxerǁ__init____mutmut_41': xǁFFMPEGMuxerǁ__init____mutmut_41, 
        'xǁFFMPEGMuxerǁ__init____mutmut_42': xǁFFMPEGMuxerǁ__init____mutmut_42, 
        'xǁFFMPEGMuxerǁ__init____mutmut_43': xǁFFMPEGMuxerǁ__init____mutmut_43, 
        'xǁFFMPEGMuxerǁ__init____mutmut_44': xǁFFMPEGMuxerǁ__init____mutmut_44, 
        'xǁFFMPEGMuxerǁ__init____mutmut_45': xǁFFMPEGMuxerǁ__init____mutmut_45, 
        'xǁFFMPEGMuxerǁ__init____mutmut_46': xǁFFMPEGMuxerǁ__init____mutmut_46, 
        'xǁFFMPEGMuxerǁ__init____mutmut_47': xǁFFMPEGMuxerǁ__init____mutmut_47, 
        'xǁFFMPEGMuxerǁ__init____mutmut_48': xǁFFMPEGMuxerǁ__init____mutmut_48, 
        'xǁFFMPEGMuxerǁ__init____mutmut_49': xǁFFMPEGMuxerǁ__init____mutmut_49, 
        'xǁFFMPEGMuxerǁ__init____mutmut_50': xǁFFMPEGMuxerǁ__init____mutmut_50, 
        'xǁFFMPEGMuxerǁ__init____mutmut_51': xǁFFMPEGMuxerǁ__init____mutmut_51, 
        'xǁFFMPEGMuxerǁ__init____mutmut_52': xǁFFMPEGMuxerǁ__init____mutmut_52, 
        'xǁFFMPEGMuxerǁ__init____mutmut_53': xǁFFMPEGMuxerǁ__init____mutmut_53, 
        'xǁFFMPEGMuxerǁ__init____mutmut_54': xǁFFMPEGMuxerǁ__init____mutmut_54, 
        'xǁFFMPEGMuxerǁ__init____mutmut_55': xǁFFMPEGMuxerǁ__init____mutmut_55, 
        'xǁFFMPEGMuxerǁ__init____mutmut_56': xǁFFMPEGMuxerǁ__init____mutmut_56, 
        'xǁFFMPEGMuxerǁ__init____mutmut_57': xǁFFMPEGMuxerǁ__init____mutmut_57, 
        'xǁFFMPEGMuxerǁ__init____mutmut_58': xǁFFMPEGMuxerǁ__init____mutmut_58, 
        'xǁFFMPEGMuxerǁ__init____mutmut_59': xǁFFMPEGMuxerǁ__init____mutmut_59, 
        'xǁFFMPEGMuxerǁ__init____mutmut_60': xǁFFMPEGMuxerǁ__init____mutmut_60, 
        'xǁFFMPEGMuxerǁ__init____mutmut_61': xǁFFMPEGMuxerǁ__init____mutmut_61, 
        'xǁFFMPEGMuxerǁ__init____mutmut_62': xǁFFMPEGMuxerǁ__init____mutmut_62, 
        'xǁFFMPEGMuxerǁ__init____mutmut_63': xǁFFMPEGMuxerǁ__init____mutmut_63, 
        'xǁFFMPEGMuxerǁ__init____mutmut_64': xǁFFMPEGMuxerǁ__init____mutmut_64, 
        'xǁFFMPEGMuxerǁ__init____mutmut_65': xǁFFMPEGMuxerǁ__init____mutmut_65, 
        'xǁFFMPEGMuxerǁ__init____mutmut_66': xǁFFMPEGMuxerǁ__init____mutmut_66, 
        'xǁFFMPEGMuxerǁ__init____mutmut_67': xǁFFMPEGMuxerǁ__init____mutmut_67, 
        'xǁFFMPEGMuxerǁ__init____mutmut_68': xǁFFMPEGMuxerǁ__init____mutmut_68, 
        'xǁFFMPEGMuxerǁ__init____mutmut_69': xǁFFMPEGMuxerǁ__init____mutmut_69, 
        'xǁFFMPEGMuxerǁ__init____mutmut_70': xǁFFMPEGMuxerǁ__init____mutmut_70, 
        'xǁFFMPEGMuxerǁ__init____mutmut_71': xǁFFMPEGMuxerǁ__init____mutmut_71, 
        'xǁFFMPEGMuxerǁ__init____mutmut_72': xǁFFMPEGMuxerǁ__init____mutmut_72, 
        'xǁFFMPEGMuxerǁ__init____mutmut_73': xǁFFMPEGMuxerǁ__init____mutmut_73, 
        'xǁFFMPEGMuxerǁ__init____mutmut_74': xǁFFMPEGMuxerǁ__init____mutmut_74, 
        'xǁFFMPEGMuxerǁ__init____mutmut_75': xǁFFMPEGMuxerǁ__init____mutmut_75, 
        'xǁFFMPEGMuxerǁ__init____mutmut_76': xǁFFMPEGMuxerǁ__init____mutmut_76, 
        'xǁFFMPEGMuxerǁ__init____mutmut_77': xǁFFMPEGMuxerǁ__init____mutmut_77, 
        'xǁFFMPEGMuxerǁ__init____mutmut_78': xǁFFMPEGMuxerǁ__init____mutmut_78, 
        'xǁFFMPEGMuxerǁ__init____mutmut_79': xǁFFMPEGMuxerǁ__init____mutmut_79, 
        'xǁFFMPEGMuxerǁ__init____mutmut_80': xǁFFMPEGMuxerǁ__init____mutmut_80, 
        'xǁFFMPEGMuxerǁ__init____mutmut_81': xǁFFMPEGMuxerǁ__init____mutmut_81, 
        'xǁFFMPEGMuxerǁ__init____mutmut_82': xǁFFMPEGMuxerǁ__init____mutmut_82, 
        'xǁFFMPEGMuxerǁ__init____mutmut_83': xǁFFMPEGMuxerǁ__init____mutmut_83, 
        'xǁFFMPEGMuxerǁ__init____mutmut_84': xǁFFMPEGMuxerǁ__init____mutmut_84, 
        'xǁFFMPEGMuxerǁ__init____mutmut_85': xǁFFMPEGMuxerǁ__init____mutmut_85, 
        'xǁFFMPEGMuxerǁ__init____mutmut_86': xǁFFMPEGMuxerǁ__init____mutmut_86, 
        'xǁFFMPEGMuxerǁ__init____mutmut_87': xǁFFMPEGMuxerǁ__init____mutmut_87, 
        'xǁFFMPEGMuxerǁ__init____mutmut_88': xǁFFMPEGMuxerǁ__init____mutmut_88, 
        'xǁFFMPEGMuxerǁ__init____mutmut_89': xǁFFMPEGMuxerǁ__init____mutmut_89, 
        'xǁFFMPEGMuxerǁ__init____mutmut_90': xǁFFMPEGMuxerǁ__init____mutmut_90, 
        'xǁFFMPEGMuxerǁ__init____mutmut_91': xǁFFMPEGMuxerǁ__init____mutmut_91, 
        'xǁFFMPEGMuxerǁ__init____mutmut_92': xǁFFMPEGMuxerǁ__init____mutmut_92, 
        'xǁFFMPEGMuxerǁ__init____mutmut_93': xǁFFMPEGMuxerǁ__init____mutmut_93, 
        'xǁFFMPEGMuxerǁ__init____mutmut_94': xǁFFMPEGMuxerǁ__init____mutmut_94, 
        'xǁFFMPEGMuxerǁ__init____mutmut_95': xǁFFMPEGMuxerǁ__init____mutmut_95, 
        'xǁFFMPEGMuxerǁ__init____mutmut_96': xǁFFMPEGMuxerǁ__init____mutmut_96, 
        'xǁFFMPEGMuxerǁ__init____mutmut_97': xǁFFMPEGMuxerǁ__init____mutmut_97, 
        'xǁFFMPEGMuxerǁ__init____mutmut_98': xǁFFMPEGMuxerǁ__init____mutmut_98, 
        'xǁFFMPEGMuxerǁ__init____mutmut_99': xǁFFMPEGMuxerǁ__init____mutmut_99, 
        'xǁFFMPEGMuxerǁ__init____mutmut_100': xǁFFMPEGMuxerǁ__init____mutmut_100, 
        'xǁFFMPEGMuxerǁ__init____mutmut_101': xǁFFMPEGMuxerǁ__init____mutmut_101, 
        'xǁFFMPEGMuxerǁ__init____mutmut_102': xǁFFMPEGMuxerǁ__init____mutmut_102, 
        'xǁFFMPEGMuxerǁ__init____mutmut_103': xǁFFMPEGMuxerǁ__init____mutmut_103, 
        'xǁFFMPEGMuxerǁ__init____mutmut_104': xǁFFMPEGMuxerǁ__init____mutmut_104, 
        'xǁFFMPEGMuxerǁ__init____mutmut_105': xǁFFMPEGMuxerǁ__init____mutmut_105, 
        'xǁFFMPEGMuxerǁ__init____mutmut_106': xǁFFMPEGMuxerǁ__init____mutmut_106, 
        'xǁFFMPEGMuxerǁ__init____mutmut_107': xǁFFMPEGMuxerǁ__init____mutmut_107, 
        'xǁFFMPEGMuxerǁ__init____mutmut_108': xǁFFMPEGMuxerǁ__init____mutmut_108, 
        'xǁFFMPEGMuxerǁ__init____mutmut_109': xǁFFMPEGMuxerǁ__init____mutmut_109, 
        'xǁFFMPEGMuxerǁ__init____mutmut_110': xǁFFMPEGMuxerǁ__init____mutmut_110, 
        'xǁFFMPEGMuxerǁ__init____mutmut_111': xǁFFMPEGMuxerǁ__init____mutmut_111, 
        'xǁFFMPEGMuxerǁ__init____mutmut_112': xǁFFMPEGMuxerǁ__init____mutmut_112, 
        'xǁFFMPEGMuxerǁ__init____mutmut_113': xǁFFMPEGMuxerǁ__init____mutmut_113, 
        'xǁFFMPEGMuxerǁ__init____mutmut_114': xǁFFMPEGMuxerǁ__init____mutmut_114, 
        'xǁFFMPEGMuxerǁ__init____mutmut_115': xǁFFMPEGMuxerǁ__init____mutmut_115, 
        'xǁFFMPEGMuxerǁ__init____mutmut_116': xǁFFMPEGMuxerǁ__init____mutmut_116, 
        'xǁFFMPEGMuxerǁ__init____mutmut_117': xǁFFMPEGMuxerǁ__init____mutmut_117, 
        'xǁFFMPEGMuxerǁ__init____mutmut_118': xǁFFMPEGMuxerǁ__init____mutmut_118, 
        'xǁFFMPEGMuxerǁ__init____mutmut_119': xǁFFMPEGMuxerǁ__init____mutmut_119, 
        'xǁFFMPEGMuxerǁ__init____mutmut_120': xǁFFMPEGMuxerǁ__init____mutmut_120, 
        'xǁFFMPEGMuxerǁ__init____mutmut_121': xǁFFMPEGMuxerǁ__init____mutmut_121, 
        'xǁFFMPEGMuxerǁ__init____mutmut_122': xǁFFMPEGMuxerǁ__init____mutmut_122, 
        'xǁFFMPEGMuxerǁ__init____mutmut_123': xǁFFMPEGMuxerǁ__init____mutmut_123, 
        'xǁFFMPEGMuxerǁ__init____mutmut_124': xǁFFMPEGMuxerǁ__init____mutmut_124, 
        'xǁFFMPEGMuxerǁ__init____mutmut_125': xǁFFMPEGMuxerǁ__init____mutmut_125, 
        'xǁFFMPEGMuxerǁ__init____mutmut_126': xǁFFMPEGMuxerǁ__init____mutmut_126, 
        'xǁFFMPEGMuxerǁ__init____mutmut_127': xǁFFMPEGMuxerǁ__init____mutmut_127, 
        'xǁFFMPEGMuxerǁ__init____mutmut_128': xǁFFMPEGMuxerǁ__init____mutmut_128, 
        'xǁFFMPEGMuxerǁ__init____mutmut_129': xǁFFMPEGMuxerǁ__init____mutmut_129, 
        'xǁFFMPEGMuxerǁ__init____mutmut_130': xǁFFMPEGMuxerǁ__init____mutmut_130, 
        'xǁFFMPEGMuxerǁ__init____mutmut_131': xǁFFMPEGMuxerǁ__init____mutmut_131, 
        'xǁFFMPEGMuxerǁ__init____mutmut_132': xǁFFMPEGMuxerǁ__init____mutmut_132, 
        'xǁFFMPEGMuxerǁ__init____mutmut_133': xǁFFMPEGMuxerǁ__init____mutmut_133, 
        'xǁFFMPEGMuxerǁ__init____mutmut_134': xǁFFMPEGMuxerǁ__init____mutmut_134, 
        'xǁFFMPEGMuxerǁ__init____mutmut_135': xǁFFMPEGMuxerǁ__init____mutmut_135, 
        'xǁFFMPEGMuxerǁ__init____mutmut_136': xǁFFMPEGMuxerǁ__init____mutmut_136, 
        'xǁFFMPEGMuxerǁ__init____mutmut_137': xǁFFMPEGMuxerǁ__init____mutmut_137, 
        'xǁFFMPEGMuxerǁ__init____mutmut_138': xǁFFMPEGMuxerǁ__init____mutmut_138, 
        'xǁFFMPEGMuxerǁ__init____mutmut_139': xǁFFMPEGMuxerǁ__init____mutmut_139, 
        'xǁFFMPEGMuxerǁ__init____mutmut_140': xǁFFMPEGMuxerǁ__init____mutmut_140, 
        'xǁFFMPEGMuxerǁ__init____mutmut_141': xǁFFMPEGMuxerǁ__init____mutmut_141, 
        'xǁFFMPEGMuxerǁ__init____mutmut_142': xǁFFMPEGMuxerǁ__init____mutmut_142, 
        'xǁFFMPEGMuxerǁ__init____mutmut_143': xǁFFMPEGMuxerǁ__init____mutmut_143, 
        'xǁFFMPEGMuxerǁ__init____mutmut_144': xǁFFMPEGMuxerǁ__init____mutmut_144, 
        'xǁFFMPEGMuxerǁ__init____mutmut_145': xǁFFMPEGMuxerǁ__init____mutmut_145, 
        'xǁFFMPEGMuxerǁ__init____mutmut_146': xǁFFMPEGMuxerǁ__init____mutmut_146, 
        'xǁFFMPEGMuxerǁ__init____mutmut_147': xǁFFMPEGMuxerǁ__init____mutmut_147, 
        'xǁFFMPEGMuxerǁ__init____mutmut_148': xǁFFMPEGMuxerǁ__init____mutmut_148, 
        'xǁFFMPEGMuxerǁ__init____mutmut_149': xǁFFMPEGMuxerǁ__init____mutmut_149, 
        'xǁFFMPEGMuxerǁ__init____mutmut_150': xǁFFMPEGMuxerǁ__init____mutmut_150, 
        'xǁFFMPEGMuxerǁ__init____mutmut_151': xǁFFMPEGMuxerǁ__init____mutmut_151, 
        'xǁFFMPEGMuxerǁ__init____mutmut_152': xǁFFMPEGMuxerǁ__init____mutmut_152, 
        'xǁFFMPEGMuxerǁ__init____mutmut_153': xǁFFMPEGMuxerǁ__init____mutmut_153, 
        'xǁFFMPEGMuxerǁ__init____mutmut_154': xǁFFMPEGMuxerǁ__init____mutmut_154, 
        'xǁFFMPEGMuxerǁ__init____mutmut_155': xǁFFMPEGMuxerǁ__init____mutmut_155, 
        'xǁFFMPEGMuxerǁ__init____mutmut_156': xǁFFMPEGMuxerǁ__init____mutmut_156, 
        'xǁFFMPEGMuxerǁ__init____mutmut_157': xǁFFMPEGMuxerǁ__init____mutmut_157, 
        'xǁFFMPEGMuxerǁ__init____mutmut_158': xǁFFMPEGMuxerǁ__init____mutmut_158, 
        'xǁFFMPEGMuxerǁ__init____mutmut_159': xǁFFMPEGMuxerǁ__init____mutmut_159, 
        'xǁFFMPEGMuxerǁ__init____mutmut_160': xǁFFMPEGMuxerǁ__init____mutmut_160, 
        'xǁFFMPEGMuxerǁ__init____mutmut_161': xǁFFMPEGMuxerǁ__init____mutmut_161, 
        'xǁFFMPEGMuxerǁ__init____mutmut_162': xǁFFMPEGMuxerǁ__init____mutmut_162, 
        'xǁFFMPEGMuxerǁ__init____mutmut_163': xǁFFMPEGMuxerǁ__init____mutmut_163, 
        'xǁFFMPEGMuxerǁ__init____mutmut_164': xǁFFMPEGMuxerǁ__init____mutmut_164, 
        'xǁFFMPEGMuxerǁ__init____mutmut_165': xǁFFMPEGMuxerǁ__init____mutmut_165, 
        'xǁFFMPEGMuxerǁ__init____mutmut_166': xǁFFMPEGMuxerǁ__init____mutmut_166, 
        'xǁFFMPEGMuxerǁ__init____mutmut_167': xǁFFMPEGMuxerǁ__init____mutmut_167, 
        'xǁFFMPEGMuxerǁ__init____mutmut_168': xǁFFMPEGMuxerǁ__init____mutmut_168, 
        'xǁFFMPEGMuxerǁ__init____mutmut_169': xǁFFMPEGMuxerǁ__init____mutmut_169, 
        'xǁFFMPEGMuxerǁ__init____mutmut_170': xǁFFMPEGMuxerǁ__init____mutmut_170, 
        'xǁFFMPEGMuxerǁ__init____mutmut_171': xǁFFMPEGMuxerǁ__init____mutmut_171, 
        'xǁFFMPEGMuxerǁ__init____mutmut_172': xǁFFMPEGMuxerǁ__init____mutmut_172, 
        'xǁFFMPEGMuxerǁ__init____mutmut_173': xǁFFMPEGMuxerǁ__init____mutmut_173, 
        'xǁFFMPEGMuxerǁ__init____mutmut_174': xǁFFMPEGMuxerǁ__init____mutmut_174, 
        'xǁFFMPEGMuxerǁ__init____mutmut_175': xǁFFMPEGMuxerǁ__init____mutmut_175, 
        'xǁFFMPEGMuxerǁ__init____mutmut_176': xǁFFMPEGMuxerǁ__init____mutmut_176, 
        'xǁFFMPEGMuxerǁ__init____mutmut_177': xǁFFMPEGMuxerǁ__init____mutmut_177, 
        'xǁFFMPEGMuxerǁ__init____mutmut_178': xǁFFMPEGMuxerǁ__init____mutmut_178, 
        'xǁFFMPEGMuxerǁ__init____mutmut_179': xǁFFMPEGMuxerǁ__init____mutmut_179, 
        'xǁFFMPEGMuxerǁ__init____mutmut_180': xǁFFMPEGMuxerǁ__init____mutmut_180, 
        'xǁFFMPEGMuxerǁ__init____mutmut_181': xǁFFMPEGMuxerǁ__init____mutmut_181, 
        'xǁFFMPEGMuxerǁ__init____mutmut_182': xǁFFMPEGMuxerǁ__init____mutmut_182, 
        'xǁFFMPEGMuxerǁ__init____mutmut_183': xǁFFMPEGMuxerǁ__init____mutmut_183, 
        'xǁFFMPEGMuxerǁ__init____mutmut_184': xǁFFMPEGMuxerǁ__init____mutmut_184, 
        'xǁFFMPEGMuxerǁ__init____mutmut_185': xǁFFMPEGMuxerǁ__init____mutmut_185, 
        'xǁFFMPEGMuxerǁ__init____mutmut_186': xǁFFMPEGMuxerǁ__init____mutmut_186, 
        'xǁFFMPEGMuxerǁ__init____mutmut_187': xǁFFMPEGMuxerǁ__init____mutmut_187
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFMPEGMuxerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFFMPEGMuxerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFFMPEGMuxerǁ__init____mutmut_orig)
    xǁFFMPEGMuxerǁ__init____mutmut_orig.__name__ = 'xǁFFMPEGMuxerǁ__init__'

    def xǁFFMPEGMuxerǁopen__mutmut_orig(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_1(self):
        for t in self.pipe_threads:
            t.daemon = None
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_2(self):
        for t in self.pipe_threads:
            t.daemon = False
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_3(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = None

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_4(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(None, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_5(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=None, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_6(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=None, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_7(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=None)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_8(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_9(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdin=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_10(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stderr=self.errorlog)

        return self

    def xǁFFMPEGMuxerǁopen__mutmut_11(self):
        for t in self.pipe_threads:
            t.daemon = True
            t.start()
        self.process = subprocess.Popen(self._cmd, stdout=subprocess.PIPE, stdin=subprocess.PIPE, )

        return self
    
    xǁFFMPEGMuxerǁopen__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFMPEGMuxerǁopen__mutmut_1': xǁFFMPEGMuxerǁopen__mutmut_1, 
        'xǁFFMPEGMuxerǁopen__mutmut_2': xǁFFMPEGMuxerǁopen__mutmut_2, 
        'xǁFFMPEGMuxerǁopen__mutmut_3': xǁFFMPEGMuxerǁopen__mutmut_3, 
        'xǁFFMPEGMuxerǁopen__mutmut_4': xǁFFMPEGMuxerǁopen__mutmut_4, 
        'xǁFFMPEGMuxerǁopen__mutmut_5': xǁFFMPEGMuxerǁopen__mutmut_5, 
        'xǁFFMPEGMuxerǁopen__mutmut_6': xǁFFMPEGMuxerǁopen__mutmut_6, 
        'xǁFFMPEGMuxerǁopen__mutmut_7': xǁFFMPEGMuxerǁopen__mutmut_7, 
        'xǁFFMPEGMuxerǁopen__mutmut_8': xǁFFMPEGMuxerǁopen__mutmut_8, 
        'xǁFFMPEGMuxerǁopen__mutmut_9': xǁFFMPEGMuxerǁopen__mutmut_9, 
        'xǁFFMPEGMuxerǁopen__mutmut_10': xǁFFMPEGMuxerǁopen__mutmut_10, 
        'xǁFFMPEGMuxerǁopen__mutmut_11': xǁFFMPEGMuxerǁopen__mutmut_11
    }
    
    def open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFMPEGMuxerǁopen__mutmut_orig"), object.__getattribute__(self, "xǁFFMPEGMuxerǁopen__mutmut_mutants"), args, kwargs, self)
        return result 
    
    open.__signature__ = _mutmut_signature(xǁFFMPEGMuxerǁopen__mutmut_orig)
    xǁFFMPEGMuxerǁopen__mutmut_orig.__name__ = 'xǁFFMPEGMuxerǁopen'

    def xǁFFMPEGMuxerǁread__mutmut_orig(self, size=-1):
        return self.process.stdout.read(size)

    def xǁFFMPEGMuxerǁread__mutmut_1(self, size=-1):
        return self.process.stdout.read(None)
    
    xǁFFMPEGMuxerǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFMPEGMuxerǁread__mutmut_1': xǁFFMPEGMuxerǁread__mutmut_1
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFMPEGMuxerǁread__mutmut_orig"), object.__getattribute__(self, "xǁFFMPEGMuxerǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁFFMPEGMuxerǁread__mutmut_orig)
    xǁFFMPEGMuxerǁread__mutmut_orig.__name__ = 'xǁFFMPEGMuxerǁread'

    def xǁFFMPEGMuxerǁclose__mutmut_orig(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_1(self):
        if self.closed:
            return

        log.debug(None)
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_2(self):
        if self.closed:
            return

        log.debug("XXClosing ffmpeg threadXX")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_3(self):
        if self.closed:
            return

        log.debug("closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_4(self):
        if self.closed:
            return

        log.debug("CLOSING FFMPEG THREAD")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_5(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = None

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_6(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = None  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_7(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(None)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_8(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(None, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_9(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, None) and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_10(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr("close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_11(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, ) and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_12(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "XXcloseXX") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_13(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "CLOSE") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_14(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "Close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_15(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") or callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_16(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(None)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_17(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(None, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_18(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=None)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_19(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_20(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, )
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_21(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug(None)

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_22(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("XXClosed all the substreamsXX")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_23(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_24(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("CLOSED ALL THE SUBSTREAMS")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_25(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = None
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_26(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get(None)
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_27(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("XXstream-timeoutXX")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_28(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("STREAM-TIMEOUT")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_29(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("Stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_30(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = None  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_31(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(None, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_32(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=None)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_33(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_34(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, )
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_35(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(None, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_36(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=None)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_37(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_38(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, )

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_39(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_40(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr or self.errorlog is not subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_41(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is subprocess.DEVNULL:
            with suppress(OSError):
                self.errorlog.close()

        super().close()

    def xǁFFMPEGMuxerǁclose__mutmut_42(self):
        if self.closed:
            return

        log.debug("Closing ffmpeg thread")
        if self.process:
            # kill ffmpeg
            self.process.kill()
            self.process.stdout.close()

            executor = concurrent.futures.ThreadPoolExecutor()

            # close the substreams
            futures = [
                executor.submit(stream.close)
                for stream in self.streams
                if hasattr(stream, "close") and callable(stream.close)
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)
            log.debug("Closed all the substreams")

            # wait for substream copy-to-pipe threads to terminate and clean up the opened pipes
            timeout = self.session.options.get("stream-timeout")
            futures = [
                executor.submit(thread.join, timeout=timeout)
                for thread in self.pipe_threads
            ]  # fmt: skip
            concurrent.futures.wait(futures, return_when=concurrent.futures.ALL_COMPLETED)

        if self.errorlog is not sys.stderr and self.errorlog is not subprocess.DEVNULL:
            with suppress(None):
                self.errorlog.close()

        super().close()
    
    xǁFFMPEGMuxerǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFMPEGMuxerǁclose__mutmut_1': xǁFFMPEGMuxerǁclose__mutmut_1, 
        'xǁFFMPEGMuxerǁclose__mutmut_2': xǁFFMPEGMuxerǁclose__mutmut_2, 
        'xǁFFMPEGMuxerǁclose__mutmut_3': xǁFFMPEGMuxerǁclose__mutmut_3, 
        'xǁFFMPEGMuxerǁclose__mutmut_4': xǁFFMPEGMuxerǁclose__mutmut_4, 
        'xǁFFMPEGMuxerǁclose__mutmut_5': xǁFFMPEGMuxerǁclose__mutmut_5, 
        'xǁFFMPEGMuxerǁclose__mutmut_6': xǁFFMPEGMuxerǁclose__mutmut_6, 
        'xǁFFMPEGMuxerǁclose__mutmut_7': xǁFFMPEGMuxerǁclose__mutmut_7, 
        'xǁFFMPEGMuxerǁclose__mutmut_8': xǁFFMPEGMuxerǁclose__mutmut_8, 
        'xǁFFMPEGMuxerǁclose__mutmut_9': xǁFFMPEGMuxerǁclose__mutmut_9, 
        'xǁFFMPEGMuxerǁclose__mutmut_10': xǁFFMPEGMuxerǁclose__mutmut_10, 
        'xǁFFMPEGMuxerǁclose__mutmut_11': xǁFFMPEGMuxerǁclose__mutmut_11, 
        'xǁFFMPEGMuxerǁclose__mutmut_12': xǁFFMPEGMuxerǁclose__mutmut_12, 
        'xǁFFMPEGMuxerǁclose__mutmut_13': xǁFFMPEGMuxerǁclose__mutmut_13, 
        'xǁFFMPEGMuxerǁclose__mutmut_14': xǁFFMPEGMuxerǁclose__mutmut_14, 
        'xǁFFMPEGMuxerǁclose__mutmut_15': xǁFFMPEGMuxerǁclose__mutmut_15, 
        'xǁFFMPEGMuxerǁclose__mutmut_16': xǁFFMPEGMuxerǁclose__mutmut_16, 
        'xǁFFMPEGMuxerǁclose__mutmut_17': xǁFFMPEGMuxerǁclose__mutmut_17, 
        'xǁFFMPEGMuxerǁclose__mutmut_18': xǁFFMPEGMuxerǁclose__mutmut_18, 
        'xǁFFMPEGMuxerǁclose__mutmut_19': xǁFFMPEGMuxerǁclose__mutmut_19, 
        'xǁFFMPEGMuxerǁclose__mutmut_20': xǁFFMPEGMuxerǁclose__mutmut_20, 
        'xǁFFMPEGMuxerǁclose__mutmut_21': xǁFFMPEGMuxerǁclose__mutmut_21, 
        'xǁFFMPEGMuxerǁclose__mutmut_22': xǁFFMPEGMuxerǁclose__mutmut_22, 
        'xǁFFMPEGMuxerǁclose__mutmut_23': xǁFFMPEGMuxerǁclose__mutmut_23, 
        'xǁFFMPEGMuxerǁclose__mutmut_24': xǁFFMPEGMuxerǁclose__mutmut_24, 
        'xǁFFMPEGMuxerǁclose__mutmut_25': xǁFFMPEGMuxerǁclose__mutmut_25, 
        'xǁFFMPEGMuxerǁclose__mutmut_26': xǁFFMPEGMuxerǁclose__mutmut_26, 
        'xǁFFMPEGMuxerǁclose__mutmut_27': xǁFFMPEGMuxerǁclose__mutmut_27, 
        'xǁFFMPEGMuxerǁclose__mutmut_28': xǁFFMPEGMuxerǁclose__mutmut_28, 
        'xǁFFMPEGMuxerǁclose__mutmut_29': xǁFFMPEGMuxerǁclose__mutmut_29, 
        'xǁFFMPEGMuxerǁclose__mutmut_30': xǁFFMPEGMuxerǁclose__mutmut_30, 
        'xǁFFMPEGMuxerǁclose__mutmut_31': xǁFFMPEGMuxerǁclose__mutmut_31, 
        'xǁFFMPEGMuxerǁclose__mutmut_32': xǁFFMPEGMuxerǁclose__mutmut_32, 
        'xǁFFMPEGMuxerǁclose__mutmut_33': xǁFFMPEGMuxerǁclose__mutmut_33, 
        'xǁFFMPEGMuxerǁclose__mutmut_34': xǁFFMPEGMuxerǁclose__mutmut_34, 
        'xǁFFMPEGMuxerǁclose__mutmut_35': xǁFFMPEGMuxerǁclose__mutmut_35, 
        'xǁFFMPEGMuxerǁclose__mutmut_36': xǁFFMPEGMuxerǁclose__mutmut_36, 
        'xǁFFMPEGMuxerǁclose__mutmut_37': xǁFFMPEGMuxerǁclose__mutmut_37, 
        'xǁFFMPEGMuxerǁclose__mutmut_38': xǁFFMPEGMuxerǁclose__mutmut_38, 
        'xǁFFMPEGMuxerǁclose__mutmut_39': xǁFFMPEGMuxerǁclose__mutmut_39, 
        'xǁFFMPEGMuxerǁclose__mutmut_40': xǁFFMPEGMuxerǁclose__mutmut_40, 
        'xǁFFMPEGMuxerǁclose__mutmut_41': xǁFFMPEGMuxerǁclose__mutmut_41, 
        'xǁFFMPEGMuxerǁclose__mutmut_42': xǁFFMPEGMuxerǁclose__mutmut_42
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFMPEGMuxerǁclose__mutmut_orig"), object.__getattribute__(self, "xǁFFMPEGMuxerǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁFFMPEGMuxerǁclose__mutmut_orig)
    xǁFFMPEGMuxerǁclose__mutmut_orig.__name__ = 'xǁFFMPEGMuxerǁclose'


class FFmpegVersionOutput(ProcessOutput):
    # The version output format of the fftools hasn't been changed since n0.7.1 (2011-04-23):
    # https://github.com/FFmpeg/FFmpeg/blame/n5.1.1/fftools/ffmpeg.c#L110
    # https://github.com/FFmpeg/FFmpeg/blame/n5.1.1/fftools/opt_common.c#L201
    # https://github.com/FFmpeg/FFmpeg/blame/c99b93c5d53d8f4a4f1fafc90f3dfc51467ee02e/fftools/cmdutils.c#L1156
    # https://github.com/FFmpeg/FFmpeg/commit/89b503b55f2b2713f1c3cc8981102c1a7b663281
    _re_version = re.compile(r"ffmpeg version (?P<version>\S+)")

    def xǁFFmpegVersionOutputǁ__init____mutmut_orig(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.version: str | None = None
        self.output: list[str] = []

    def xǁFFmpegVersionOutputǁ__init____mutmut_1(self, *args, **kwargs) -> None:
        super().__init__(**kwargs)
        self.version: str | None = None
        self.output: list[str] = []

    def xǁFFmpegVersionOutputǁ__init____mutmut_2(self, *args, **kwargs) -> None:
        super().__init__(*args, )
        self.version: str | None = None
        self.output: list[str] = []

    def xǁFFmpegVersionOutputǁ__init____mutmut_3(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.version: str | None = ""
        self.output: list[str] = []

    def xǁFFmpegVersionOutputǁ__init____mutmut_4(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.version: str | None = None
        self.output: list[str] = None
    
    xǁFFmpegVersionOutputǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFmpegVersionOutputǁ__init____mutmut_1': xǁFFmpegVersionOutputǁ__init____mutmut_1, 
        'xǁFFmpegVersionOutputǁ__init____mutmut_2': xǁFFmpegVersionOutputǁ__init____mutmut_2, 
        'xǁFFmpegVersionOutputǁ__init____mutmut_3': xǁFFmpegVersionOutputǁ__init____mutmut_3, 
        'xǁFFmpegVersionOutputǁ__init____mutmut_4': xǁFFmpegVersionOutputǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFmpegVersionOutputǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFFmpegVersionOutputǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFFmpegVersionOutputǁ__init____mutmut_orig)
    xǁFFmpegVersionOutputǁ__init____mutmut_orig.__name__ = 'xǁFFmpegVersionOutputǁ__init__'

    def xǁFFmpegVersionOutputǁonexit__mutmut_orig(self, code: int) -> bool:
        return code == 0 and self.version is not None

    def xǁFFmpegVersionOutputǁonexit__mutmut_1(self, code: int) -> bool:
        return code != 0 and self.version is not None

    def xǁFFmpegVersionOutputǁonexit__mutmut_2(self, code: int) -> bool:
        return code == 1 and self.version is not None

    def xǁFFmpegVersionOutputǁonexit__mutmut_3(self, code: int) -> bool:
        return code == 0 or self.version is not None

    def xǁFFmpegVersionOutputǁonexit__mutmut_4(self, code: int) -> bool:
        return code == 0 and self.version is None
    
    xǁFFmpegVersionOutputǁonexit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFmpegVersionOutputǁonexit__mutmut_1': xǁFFmpegVersionOutputǁonexit__mutmut_1, 
        'xǁFFmpegVersionOutputǁonexit__mutmut_2': xǁFFmpegVersionOutputǁonexit__mutmut_2, 
        'xǁFFmpegVersionOutputǁonexit__mutmut_3': xǁFFmpegVersionOutputǁonexit__mutmut_3, 
        'xǁFFmpegVersionOutputǁonexit__mutmut_4': xǁFFmpegVersionOutputǁonexit__mutmut_4
    }
    
    def onexit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFmpegVersionOutputǁonexit__mutmut_orig"), object.__getattribute__(self, "xǁFFmpegVersionOutputǁonexit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    onexit.__signature__ = _mutmut_signature(xǁFFmpegVersionOutputǁonexit__mutmut_orig)
    xǁFFmpegVersionOutputǁonexit__mutmut_orig.__name__ = 'xǁFFmpegVersionOutputǁonexit'

    def xǁFFmpegVersionOutputǁonstdout__mutmut_orig(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_1(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx != 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_2(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 1:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_3(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = None
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_4(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(None)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_5(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if match:
                return False
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_6(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return True
            self.version = match["version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_7(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = None

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_8(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["XXversionXX"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_9(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["VERSION"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_10(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["Version"]

        self.output.append(line)

    def xǁFFmpegVersionOutputǁonstdout__mutmut_11(self, idx: int, line: str) -> bool | None:
        # only validate the very first line of the stdout stream
        if idx == 0:
            match = self._re_version.match(line)
            # abort if the very first line of stdout doesn't match the expected format
            if not match:
                return False
            self.version = match["version"]

        self.output.append(None)
    
    xǁFFmpegVersionOutputǁonstdout__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFFmpegVersionOutputǁonstdout__mutmut_1': xǁFFmpegVersionOutputǁonstdout__mutmut_1, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_2': xǁFFmpegVersionOutputǁonstdout__mutmut_2, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_3': xǁFFmpegVersionOutputǁonstdout__mutmut_3, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_4': xǁFFmpegVersionOutputǁonstdout__mutmut_4, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_5': xǁFFmpegVersionOutputǁonstdout__mutmut_5, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_6': xǁFFmpegVersionOutputǁonstdout__mutmut_6, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_7': xǁFFmpegVersionOutputǁonstdout__mutmut_7, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_8': xǁFFmpegVersionOutputǁonstdout__mutmut_8, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_9': xǁFFmpegVersionOutputǁonstdout__mutmut_9, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_10': xǁFFmpegVersionOutputǁonstdout__mutmut_10, 
        'xǁFFmpegVersionOutputǁonstdout__mutmut_11': xǁFFmpegVersionOutputǁonstdout__mutmut_11
    }
    
    def onstdout(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFFmpegVersionOutputǁonstdout__mutmut_orig"), object.__getattribute__(self, "xǁFFmpegVersionOutputǁonstdout__mutmut_mutants"), args, kwargs, self)
        return result 
    
    onstdout.__signature__ = _mutmut_signature(xǁFFmpegVersionOutputǁonstdout__mutmut_orig)
    xǁFFmpegVersionOutputǁonstdout__mutmut_orig.__name__ = 'xǁFFmpegVersionOutputǁonstdout'

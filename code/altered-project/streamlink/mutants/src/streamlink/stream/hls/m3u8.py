from __future__ import annotations

import logging
import math
import re
from binascii import Error as BinasciiError, unhexlify
from collections.abc import Callable, Iterator, Mapping
from datetime import datetime, timedelta
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar
from urllib.parse import urljoin, urlparse

from isodate import ISO8601Error, parse_datetime  # type: ignore[import]
from requests import Response

from streamlink.logger import ALL, StreamlinkLogger
from streamlink.stream.hls.segment import (
    ByteRange,
    DateRange,
    ExtInf,
    HLSPlaylist,
    HLSSegment,
    IFrameStreamInfo,
    Key,
    Map,
    Media,
    Resolution,
    Start,
    StreamInfo,
)


if TYPE_CHECKING:
    try:
        from typing import Self  # type: ignore[attr-defined]
    except ImportError:
        from typing_extensions import Self


log: StreamlinkLogger = logging.getLogger(__name__)  # type: ignore[assignment]


THLSSegment_co = TypeVar("THLSSegment_co", bound=HLSSegment, covariant=True)
THLSPlaylist_co = TypeVar("THLSPlaylist_co", bound=HLSPlaylist, covariant=True)
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


class M3U8(Generic[THLSSegment_co, THLSPlaylist_co]):
    def xǁM3U8ǁ__init____mutmut_orig(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_1(self, uri: str | None = None):
        self.uri = None

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_2(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = None
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_3(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = True
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_4(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = None

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_5(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = True

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_6(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = ""  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_7(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = ""
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_8(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = ""  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_9(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = ""
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_10(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = ""
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_11(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = ""
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_12(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = ""
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_13(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = ""

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_14(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = None
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_15(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = None

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_16(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = None
        self.segments: list[THLSSegment_co] = []
    def xǁM3U8ǁ__init____mutmut_17(self, uri: str | None = None):
        self.uri = uri

        self.is_endlist: bool = False
        self.is_master: bool = False

        self.allow_cache: bool | None = None  # version < 7
        self.discontinuity_sequence: int | None = None
        self.iframes_only: bool | None = None  # version >= 4
        self.media_sequence: int | None = None
        self.playlist_type: str | None = None
        self.targetduration: float | None = None
        self.start: Start | None = None
        self.version: int | None = None

        self.media: list[Media] = []
        self.dateranges: list[DateRange] = []

        self.playlists: list[THLSPlaylist_co] = []
        self.segments: list[THLSSegment_co] = None
    
    xǁM3U8ǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8ǁ__init____mutmut_1': xǁM3U8ǁ__init____mutmut_1, 
        'xǁM3U8ǁ__init____mutmut_2': xǁM3U8ǁ__init____mutmut_2, 
        'xǁM3U8ǁ__init____mutmut_3': xǁM3U8ǁ__init____mutmut_3, 
        'xǁM3U8ǁ__init____mutmut_4': xǁM3U8ǁ__init____mutmut_4, 
        'xǁM3U8ǁ__init____mutmut_5': xǁM3U8ǁ__init____mutmut_5, 
        'xǁM3U8ǁ__init____mutmut_6': xǁM3U8ǁ__init____mutmut_6, 
        'xǁM3U8ǁ__init____mutmut_7': xǁM3U8ǁ__init____mutmut_7, 
        'xǁM3U8ǁ__init____mutmut_8': xǁM3U8ǁ__init____mutmut_8, 
        'xǁM3U8ǁ__init____mutmut_9': xǁM3U8ǁ__init____mutmut_9, 
        'xǁM3U8ǁ__init____mutmut_10': xǁM3U8ǁ__init____mutmut_10, 
        'xǁM3U8ǁ__init____mutmut_11': xǁM3U8ǁ__init____mutmut_11, 
        'xǁM3U8ǁ__init____mutmut_12': xǁM3U8ǁ__init____mutmut_12, 
        'xǁM3U8ǁ__init____mutmut_13': xǁM3U8ǁ__init____mutmut_13, 
        'xǁM3U8ǁ__init____mutmut_14': xǁM3U8ǁ__init____mutmut_14, 
        'xǁM3U8ǁ__init____mutmut_15': xǁM3U8ǁ__init____mutmut_15, 
        'xǁM3U8ǁ__init____mutmut_16': xǁM3U8ǁ__init____mutmut_16, 
        'xǁM3U8ǁ__init____mutmut_17': xǁM3U8ǁ__init____mutmut_17
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8ǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁM3U8ǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁM3U8ǁ__init____mutmut_orig)
    xǁM3U8ǁ__init____mutmut_orig.__name__ = 'xǁM3U8ǁ__init__'

    @classmethod
    def is_date_in_daterange(cls, date: datetime | None, daterange: DateRange):
        if date is None or daterange.start_date is None:
            return None

        if daterange.end_date is not None:
            return daterange.start_date <= date < daterange.end_date

        duration = daterange.duration or daterange.planned_duration
        if duration is not None:
            end = daterange.start_date + duration
            return daterange.start_date <= date < end

        return daterange.start_date <= date


TM3U8_co = TypeVar("TM3U8_co", bound=M3U8, covariant=True)


_symbol_tag_parser = "__PARSE_TAG_NAME"


def x_parse_tag__mutmut_orig(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(func, _symbol_tag_parser, tag)

        return func

    return decorator


def x_parse_tag__mutmut_1(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(None, _symbol_tag_parser, tag)

        return func

    return decorator


def x_parse_tag__mutmut_2(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(func, None, tag)

        return func

    return decorator


def x_parse_tag__mutmut_3(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(func, _symbol_tag_parser, None)

        return func

    return decorator


def x_parse_tag__mutmut_4(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(_symbol_tag_parser, tag)

        return func

    return decorator


def x_parse_tag__mutmut_5(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(func, tag)

        return func

    return decorator


def x_parse_tag__mutmut_6(tag: str):
    def decorator(func: Callable[[str], None]) -> Callable[[str], None]:
        setattr(func, _symbol_tag_parser, )

        return func

    return decorator

x_parse_tag__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_tag__mutmut_1': x_parse_tag__mutmut_1, 
    'x_parse_tag__mutmut_2': x_parse_tag__mutmut_2, 
    'x_parse_tag__mutmut_3': x_parse_tag__mutmut_3, 
    'x_parse_tag__mutmut_4': x_parse_tag__mutmut_4, 
    'x_parse_tag__mutmut_5': x_parse_tag__mutmut_5, 
    'x_parse_tag__mutmut_6': x_parse_tag__mutmut_6
}

def parse_tag(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_tag__mutmut_orig, x_parse_tag__mutmut_mutants, args, kwargs)
    return result 

parse_tag.__signature__ = _mutmut_signature(x_parse_tag__mutmut_orig)
x_parse_tag__mutmut_orig.__name__ = 'x_parse_tag'


class M3U8ParserMeta(type):
    def xǁM3U8ParserMetaǁ__init____mutmut_orig(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_1(cls, name, bases, namespace, **kwargs):
        super().__init__(None, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_2(cls, name, bases, namespace, **kwargs):
        super().__init__(name, None, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_3(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, None, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_4(cls, name, bases, namespace, **kwargs):
        super().__init__(bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_5(cls, name, bases, namespace, **kwargs):
        super().__init__(name, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_6(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_7(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, )

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_8(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = None
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_9(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(None, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_10(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, None, {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_11(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", None))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_12(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr("_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_13(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_14(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", ))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_15(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "XX_TAGSXX", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_16(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_tags", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_17(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_tags", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_18(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = None
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_19(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(None, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_20(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, None, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_21(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(_symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_22(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_23(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, )
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_24(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(None) is not str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_25(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is str:
                continue
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_26(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                break
            tags[tag] = member
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_27(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = None
        cls._TAGS = tags
    def xǁM3U8ParserMetaǁ__init____mutmut_28(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace, **kwargs)

        tags = dict(**getattr(cls, "_TAGS", {}))
        for member in namespace.values():
            tag = getattr(member, _symbol_tag_parser, None)
            if type(tag) is not str:
                continue
            tags[tag] = member
        cls._TAGS = None
    
    xǁM3U8ParserMetaǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8ParserMetaǁ__init____mutmut_1': xǁM3U8ParserMetaǁ__init____mutmut_1, 
        'xǁM3U8ParserMetaǁ__init____mutmut_2': xǁM3U8ParserMetaǁ__init____mutmut_2, 
        'xǁM3U8ParserMetaǁ__init____mutmut_3': xǁM3U8ParserMetaǁ__init____mutmut_3, 
        'xǁM3U8ParserMetaǁ__init____mutmut_4': xǁM3U8ParserMetaǁ__init____mutmut_4, 
        'xǁM3U8ParserMetaǁ__init____mutmut_5': xǁM3U8ParserMetaǁ__init____mutmut_5, 
        'xǁM3U8ParserMetaǁ__init____mutmut_6': xǁM3U8ParserMetaǁ__init____mutmut_6, 
        'xǁM3U8ParserMetaǁ__init____mutmut_7': xǁM3U8ParserMetaǁ__init____mutmut_7, 
        'xǁM3U8ParserMetaǁ__init____mutmut_8': xǁM3U8ParserMetaǁ__init____mutmut_8, 
        'xǁM3U8ParserMetaǁ__init____mutmut_9': xǁM3U8ParserMetaǁ__init____mutmut_9, 
        'xǁM3U8ParserMetaǁ__init____mutmut_10': xǁM3U8ParserMetaǁ__init____mutmut_10, 
        'xǁM3U8ParserMetaǁ__init____mutmut_11': xǁM3U8ParserMetaǁ__init____mutmut_11, 
        'xǁM3U8ParserMetaǁ__init____mutmut_12': xǁM3U8ParserMetaǁ__init____mutmut_12, 
        'xǁM3U8ParserMetaǁ__init____mutmut_13': xǁM3U8ParserMetaǁ__init____mutmut_13, 
        'xǁM3U8ParserMetaǁ__init____mutmut_14': xǁM3U8ParserMetaǁ__init____mutmut_14, 
        'xǁM3U8ParserMetaǁ__init____mutmut_15': xǁM3U8ParserMetaǁ__init____mutmut_15, 
        'xǁM3U8ParserMetaǁ__init____mutmut_16': xǁM3U8ParserMetaǁ__init____mutmut_16, 
        'xǁM3U8ParserMetaǁ__init____mutmut_17': xǁM3U8ParserMetaǁ__init____mutmut_17, 
        'xǁM3U8ParserMetaǁ__init____mutmut_18': xǁM3U8ParserMetaǁ__init____mutmut_18, 
        'xǁM3U8ParserMetaǁ__init____mutmut_19': xǁM3U8ParserMetaǁ__init____mutmut_19, 
        'xǁM3U8ParserMetaǁ__init____mutmut_20': xǁM3U8ParserMetaǁ__init____mutmut_20, 
        'xǁM3U8ParserMetaǁ__init____mutmut_21': xǁM3U8ParserMetaǁ__init____mutmut_21, 
        'xǁM3U8ParserMetaǁ__init____mutmut_22': xǁM3U8ParserMetaǁ__init____mutmut_22, 
        'xǁM3U8ParserMetaǁ__init____mutmut_23': xǁM3U8ParserMetaǁ__init____mutmut_23, 
        'xǁM3U8ParserMetaǁ__init____mutmut_24': xǁM3U8ParserMetaǁ__init____mutmut_24, 
        'xǁM3U8ParserMetaǁ__init____mutmut_25': xǁM3U8ParserMetaǁ__init____mutmut_25, 
        'xǁM3U8ParserMetaǁ__init____mutmut_26': xǁM3U8ParserMetaǁ__init____mutmut_26, 
        'xǁM3U8ParserMetaǁ__init____mutmut_27': xǁM3U8ParserMetaǁ__init____mutmut_27, 
        'xǁM3U8ParserMetaǁ__init____mutmut_28': xǁM3U8ParserMetaǁ__init____mutmut_28
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8ParserMetaǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁM3U8ParserMetaǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁM3U8ParserMetaǁ__init____mutmut_orig)
    xǁM3U8ParserMetaǁ__init____mutmut_orig.__name__ = 'xǁM3U8ParserMetaǁ__init__'


class M3U8Parser(Generic[TM3U8_co, THLSSegment_co, THLSPlaylist_co], metaclass=M3U8ParserMeta):
    # Can't set type vars as classvars yet (PEP 526 issue)
    __m3u8__: ClassVar[type[M3U8[HLSSegment, HLSPlaylist]]] = M3U8
    __segment__: ClassVar[type[HLSSegment]] = HLSSegment
    __playlist__: ClassVar[type[HLSPlaylist]] = HLSPlaylist

    _TAGS: ClassVar[Mapping[str, Callable[[Self, str], None]]]

    _extinf_re = re.compile(r"(?P<duration>\d+(\.\d+)?)(,(?P<title>.+))?")
    _attr_re = re.compile(
        r"""
            (?P<key>[A-Z0-9\-]+)
            =
            (?P<value>
                (?# decimal-integer)
                \d+
                (?# hexadecimal-sequence)
                |0[xX][0-9A-Fa-f]+
                (?# decimal-floating-point and signed-decimal-floating-point)
                |-?\d+\.\d+
                (?# quoted-string)
                |\"(?P<quoted>[^\r\n\"]*)\"
                (?# enumerated-string)
                |[^\",\s]+
                (?# decimal-resolution)
                |\d+x\d+
            )
            (?# be more lenient and allow spaces around attributes)
            \s*(?:,\s*|$)
        """,
        re.VERBOSE,
    )
    _range_re = re.compile(r"(?P<range>\d+)(?:@(?P<offset>\d+))?")
    _tag_re = re.compile(r"#(?P<tag>[\w-]+)(:(?P<value>.+))?")
    _res_re = re.compile(r"(\d+)x(\d+)")

    def xǁM3U8Parserǁ__init____mutmut_orig(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_1(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = None  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_2(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(None)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_3(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = None
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_4(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = True
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_5(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = ""

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_6(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = None
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_7(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = True
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_8(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = ""
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_9(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = ""
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_10(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = None
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_11(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = True
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_12(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = ""
        self._key: Key | None = None
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_13(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = ""
        self._date: datetime | None = None

    def xǁM3U8Parserǁ__init____mutmut_14(self, base_uri: str | None = None):
        self.m3u8: TM3U8_co = self.__m3u8__(base_uri)  # type: ignore[assignment]  # PEP 696 might solve this

        self._expect_playlist: bool = False
        self._streaminf: dict[str, str] | None = None

        self._expect_segment: bool = False
        self._extinf: ExtInf | None = None
        self._byterange: ByteRange | None = None
        self._discontinuity: bool = False
        self._map: Map | None = None
        self._key: Key | None = None
        self._date: datetime | None = ""
    
    xǁM3U8Parserǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁ__init____mutmut_1': xǁM3U8Parserǁ__init____mutmut_1, 
        'xǁM3U8Parserǁ__init____mutmut_2': xǁM3U8Parserǁ__init____mutmut_2, 
        'xǁM3U8Parserǁ__init____mutmut_3': xǁM3U8Parserǁ__init____mutmut_3, 
        'xǁM3U8Parserǁ__init____mutmut_4': xǁM3U8Parserǁ__init____mutmut_4, 
        'xǁM3U8Parserǁ__init____mutmut_5': xǁM3U8Parserǁ__init____mutmut_5, 
        'xǁM3U8Parserǁ__init____mutmut_6': xǁM3U8Parserǁ__init____mutmut_6, 
        'xǁM3U8Parserǁ__init____mutmut_7': xǁM3U8Parserǁ__init____mutmut_7, 
        'xǁM3U8Parserǁ__init____mutmut_8': xǁM3U8Parserǁ__init____mutmut_8, 
        'xǁM3U8Parserǁ__init____mutmut_9': xǁM3U8Parserǁ__init____mutmut_9, 
        'xǁM3U8Parserǁ__init____mutmut_10': xǁM3U8Parserǁ__init____mutmut_10, 
        'xǁM3U8Parserǁ__init____mutmut_11': xǁM3U8Parserǁ__init____mutmut_11, 
        'xǁM3U8Parserǁ__init____mutmut_12': xǁM3U8Parserǁ__init____mutmut_12, 
        'xǁM3U8Parserǁ__init____mutmut_13': xǁM3U8Parserǁ__init____mutmut_13, 
        'xǁM3U8Parserǁ__init____mutmut_14': xǁM3U8Parserǁ__init____mutmut_14
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁM3U8Parserǁ__init____mutmut_orig)
    xǁM3U8Parserǁ__init____mutmut_orig.__name__ = 'xǁM3U8Parserǁ__init__'

    @classmethod
    def create_stream_info(cls, streaminf: Mapping[str, str | None], streaminfoclass=None):
        program_id = streaminf.get("PROGRAM-ID")

        try:
            bandwidth = int(streaminf.get("BANDWIDTH") or 0)
            bandwidth = round(bandwidth, 1 - int(math.log10(bandwidth)))
        except ValueError:
            bandwidth = 0

        res = streaminf.get("RESOLUTION")
        resolution = None if not res else cls.parse_resolution(res)

        codecs = (streaminf.get("CODECS") or "").split(",")

        if streaminfoclass is IFrameStreamInfo:
            return IFrameStreamInfo(
                bandwidth=bandwidth,
                program_id=program_id,
                codecs=codecs,
                resolution=resolution,
                video=streaminf.get("VIDEO"),
            )
        else:
            return StreamInfo(
                bandwidth=bandwidth,
                program_id=program_id,
                codecs=codecs,
                resolution=resolution,
                audio=streaminf.get("AUDIO"),
                video=streaminf.get("VIDEO"),
                subtitles=streaminf.get("SUBTITLES"),
            )

    @classmethod
    def split_tag(cls, line: str) -> tuple[str, str] | tuple[None, None]:
        match = cls._tag_re.match(line)

        if match:
            return match.group("tag"), (match.group("value") or "").strip()

        return None, None

    @classmethod
    def parse_attributes(cls, value: str) -> dict[str, str]:
        pos = 0
        length = len(value)
        res: dict[str, str] = {}
        while pos < length:
            match = cls._attr_re.match(value, pos)
            if match is None:
                log.warning("Discarded invalid attributes list")
                res.clear()
                break
            pos = match.end()
            res[match["key"]] = match["quoted"] if match["quoted"] is not None else match["value"]

        return res

    @staticmethod
    def parse_bool(value: str) -> bool:
        return value == "YES"

    @classmethod
    def parse_byterange(cls, value: str) -> ByteRange | None:
        match = cls._range_re.match(value)
        if match is None:
            return None

        offset = match["offset"]

        return ByteRange(
            range=int(match["range"]),
            offset=int(offset) if offset is not None else None,
        )

    @classmethod
    def parse_extinf(cls, value: str) -> ExtInf:
        match = cls._extinf_re.match(value)
        if match is None:
            return ExtInf(0, None)

        return ExtInf(
            duration=float(match.group("duration")),
            title=match.group("title"),
        )

    @staticmethod
    def parse_hex(value: str | None) -> bytes | None:
        if value is None:
            return None

        if value[:2] in ("0x", "0X"):
            try:
                return unhexlify(f"{'0' * (len(value) % 2)}{value[2:]}")
            except BinasciiError:
                pass

        log.warning("Discarded invalid hexadecimal-sequence attribute value")
        return None

    @staticmethod
    def parse_iso8601(value: str | None) -> datetime | None:
        try:
            return None if value is None else parse_datetime(value)
        except (ISO8601Error, ValueError):
            log.warning("Discarded invalid ISO8601 attribute value")
            return None

    @staticmethod
    def parse_timedelta(value: str | None) -> timedelta | None:
        return None if value is None else timedelta(seconds=float(value))

    @classmethod
    def parse_resolution(cls, value: str) -> Resolution:
        match = cls._res_re.match(value)
        if match is None:
            return Resolution(width=0, height=0)

        return Resolution(
            width=int(match.group(1)),
            height=int(match.group(2)),
        )

    # ----

    # 4.3.1: Basic Tags

    @parse_tag("EXT-X-VERSION")
    def parse_tag_ext_x_version(self, value: str) -> None:
        """
        EXT-X-VERSION
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.1.2
        """
        self.m3u8.version = int(value)

    # 4.3.2: Media Segment Tags

    @parse_tag("EXTINF")
    def parse_tag_extinf(self, value: str) -> None:
        """
        EXTINF
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.1
        """
        self._expect_segment = True
        self._extinf = self.parse_extinf(value)

    @parse_tag("EXT-X-BYTERANGE")
    def parse_tag_ext_x_byterange(self, value: str) -> None:
        """
        EXT-X-BYTERANGE
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.2
        """
        self._expect_segment = True
        self._byterange = self.parse_byterange(value)

    # noinspection PyUnusedLocal
    @parse_tag("EXT-X-DISCONTINUITY")
    def parse_tag_ext_x_discontinuity(self, value: str) -> None:
        """
        EXT-X-DISCONTINUITY
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.3
        """
        self._discontinuity = True
        self._map = None

    @parse_tag("EXT-X-KEY")
    def parse_tag_ext_x_key(self, value: str) -> None:
        """
        EXT-X-KEY
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.4
        """
        attr = self.parse_attributes(value)
        method = attr.get("METHOD")
        uri = attr.get("URI")

        if not method:
            return

        self._key = Key(
            method=method,
            uri=self.uri(uri) if uri else None,
            iv=self.parse_hex(attr.get("IV")),
            key_format=attr.get("KEYFORMAT"),
            key_format_versions=attr.get("KEYFORMATVERSIONS"),
        )

    @parse_tag("EXT-X-MAP")
    def parse_tag_ext_x_map(self, value: str) -> None:  # version >= 5
        """
        EXT-X-MAP
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.5
        """
        attr = self.parse_attributes(value)
        uri = attr.get("URI")

        if not uri:
            return

        byterange = self.parse_byterange(attr.get("BYTERANGE", ""))
        self._map = Map(
            uri=self.uri(uri),
            key=self._key,
            byterange=byterange,
        )

    @parse_tag("EXT-X-PROGRAM-DATE-TIME")
    def parse_tag_ext_x_program_date_time(self, value: str) -> None:
        """
        EXT-X-PROGRAM-DATE-TIME
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.6
        """
        self._date = self.parse_iso8601(value)

    @parse_tag("EXT-X-DATERANGE")
    def parse_tag_ext_x_daterange(self, value: str) -> None:
        """
        EXT-X-DATERANGE
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.2.7
        """
        attr = self.parse_attributes(value)
        daterange = DateRange(
            id=attr.pop("ID", None),
            classname=attr.pop("CLASS", None),
            start_date=self.parse_iso8601(attr.pop("START-DATE", None)),
            end_date=self.parse_iso8601(attr.pop("END-DATE", None)),
            duration=self.parse_timedelta(attr.pop("DURATION", None)),
            planned_duration=self.parse_timedelta(attr.pop("PLANNED-DURATION", None)),
            end_on_next=self.parse_bool(attr.pop("END-ON-NEXT", "NO")),
            x=attr,
        )
        self.m3u8.dateranges.append(daterange)

    # 4.3.3: Media Playlist Tags

    @parse_tag("EXT-X-TARGETDURATION")
    def parse_tag_ext_x_targetduration(self, value: str) -> None:
        """
        EXT-X-TARGETDURATION
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.1
        """
        self.m3u8.targetduration = float(value)

    @parse_tag("EXT-X-MEDIA-SEQUENCE")
    def parse_tag_ext_x_media_sequence(self, value: str) -> None:
        """
        EXT-X-MEDIA-SEQUENCE
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.2
        """
        self.m3u8.media_sequence = int(value)

    @parse_tag("EXT-X-DISCONTINUTY-SEQUENCE")
    def parse_tag_ext_x_discontinuity_sequence(self, value: str) -> None:
        """
        EXT-X-DISCONTINUITY-SEQUENCE
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.3
        """
        self.m3u8.discontinuity_sequence = int(value)

    # noinspection PyUnusedLocal
    @parse_tag("EXT-X-ENDLIST")
    def parse_tag_ext_x_endlist(self, value: str) -> None:
        """
        EXT-X-ENDLIST
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.4
        """
        self.m3u8.is_endlist = True

    @parse_tag("EXT-X-PLAYLIST-TYPE")
    def parse_tag_ext_x_playlist_type(self, value: str) -> None:
        """
        EXT-X-PLAYLISTTYPE
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.5
        """
        self.m3u8.playlist_type = value

    # noinspection PyUnusedLocal
    @parse_tag("EXT-X-I-FRAMES-ONLY")
    def parse_tag_ext_x_i_frames_only(self, value: str) -> None:  # version >= 4
        """
        EXT-X-I-FRAMES-ONLY
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.3.6
        """
        self.m3u8.iframes_only = True

    # 4.3.4: Master Playlist Tags

    @parse_tag("EXT-X-MEDIA")
    def parse_tag_ext_x_media(self, value: str) -> None:
        """
        EXT-X-MEDIA
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.4.1
        """
        attr = self.parse_attributes(value)
        mediatype = attr.get("TYPE")
        uri = attr.get("URI")
        group_id = attr.get("GROUP-ID")
        name = attr.get("NAME")

        if not mediatype or not group_id or not name:
            return

        if language := attr.get("LANGUAGE"):
            language = language.strip().lower()

        media = Media(
            type=mediatype,
            uri=self.uri(uri) if uri else None,
            group_id=group_id,
            language=language,
            name=name,
            default=self.parse_bool(attr.get("DEFAULT", "NO")),
            autoselect=self.parse_bool(attr.get("AUTOSELECT", "NO")),
            forced=self.parse_bool(attr.get("FORCED", "NO")),
            characteristics=attr.get("CHARACTERISTICS"),
        )
        self.m3u8.media.append(media)

    @parse_tag("EXT-X-STREAM-INF")
    def parse_tag_ext_x_stream_inf(self, value: str) -> None:
        """
        EXT-X-STREAM-INF
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.4.2
        """
        self._expect_playlist = True
        self._streaminf = self.parse_attributes(value)

    @parse_tag("EXT-X-I-FRAME-STREAM-INF")
    def parse_tag_ext_x_i_frame_stream_inf(self, value: str) -> None:
        """
        EXT-X-I-FRAME-STREAM-INF
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.4.3
        """
        attr = self.parse_attributes(value)
        uri = attr.get("URI")

        streaminf = self._streaminf or attr
        self._streaminf = None

        if not uri:
            return

        stream_info = self.create_stream_info(streaminf, IFrameStreamInfo)
        playlist = HLSPlaylist(
            uri=self.uri(uri),
            stream_info=stream_info,
            media=[],
            is_iframe=True,
        )
        self.m3u8.playlists.append(playlist)

    @parse_tag("EXT-X-SESSION-DATA")
    def parse_tag_ext_x_session_data(self, value: str) -> None:
        """
        EXT-X-SESSION-DATA
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.4.4
        """

    @parse_tag("EXT-X-SESSION-KEY")
    def parse_tag_ext_x_session_key(self, value: str) -> None:
        """
        EXT-X-SESSION-KEY
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.4.5
        """

    # 4.3.5: Media or Master Playlist Tags

    @parse_tag("EXT-X-INDEPENDENT-SEGMENTS")
    def parse_tag_ext_x_independent_segments(self, value: str) -> None:
        """
        EXT-X-INDEPENDENT-SEGMENTS
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.5.1
        """

    @parse_tag("EXT-X-START")
    def parse_tag_ext_x_start(self, value: str) -> None:
        """
        EXT-X-START
        https://datatracker.ietf.org/doc/html/rfc8216#section-4.3.5.2
        """
        attr = self.parse_attributes(value)
        self.m3u8.start = Start(
            time_offset=float(attr.get("TIME-OFFSET", 0)),
            precise=self.parse_bool(attr.get("PRECISE", "NO")),
        )

    # Removed tags
    # https://datatracker.ietf.org/doc/html/rfc8216#section-7

    @parse_tag("EXT-X-ALLOW-CACHE")
    def parse_tag_ext_x_allow_cache(self, value: str) -> None:  # version < 7
        self.m3u8.allow_cache = self.parse_bool(value)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_orig(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_1(self, line: str) -> None:
        if line.startswith(None):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_2(self, line: str) -> None:
        if line.startswith("XX#XX"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_3(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = None
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_4(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(None)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_5(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_6(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag and value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_7(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is not None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_8(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None and tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_9(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_10(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](None, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_11(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, None)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_12(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_13(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, )

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_14(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = None
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_15(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = True
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_16(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = None
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_17(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(None)
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_18(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(None))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_19(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(None)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_20(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = None
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_21(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = True
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_22(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = None
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_23(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(None)
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_24(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(None))
            self.m3u8.playlists.append(playlist)

    # ----

    def xǁM3U8Parserǁparse_line__mutmut_25(self, line: str) -> None:
        if line.startswith("#"):
            tag, value = self.split_tag(line)
            if not tag or value is None or tag not in self._TAGS:
                return
            self._TAGS[tag](self, value)

        elif self._expect_segment:
            self._expect_segment = False
            segment = self.get_segment(self.uri(line))
            self.m3u8.segments.append(segment)

        elif self._expect_playlist:
            self._expect_playlist = False
            playlist = self.get_playlist(self.uri(line))
            self.m3u8.playlists.append(None)
    
    xǁM3U8Parserǁparse_line__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁparse_line__mutmut_1': xǁM3U8Parserǁparse_line__mutmut_1, 
        'xǁM3U8Parserǁparse_line__mutmut_2': xǁM3U8Parserǁparse_line__mutmut_2, 
        'xǁM3U8Parserǁparse_line__mutmut_3': xǁM3U8Parserǁparse_line__mutmut_3, 
        'xǁM3U8Parserǁparse_line__mutmut_4': xǁM3U8Parserǁparse_line__mutmut_4, 
        'xǁM3U8Parserǁparse_line__mutmut_5': xǁM3U8Parserǁparse_line__mutmut_5, 
        'xǁM3U8Parserǁparse_line__mutmut_6': xǁM3U8Parserǁparse_line__mutmut_6, 
        'xǁM3U8Parserǁparse_line__mutmut_7': xǁM3U8Parserǁparse_line__mutmut_7, 
        'xǁM3U8Parserǁparse_line__mutmut_8': xǁM3U8Parserǁparse_line__mutmut_8, 
        'xǁM3U8Parserǁparse_line__mutmut_9': xǁM3U8Parserǁparse_line__mutmut_9, 
        'xǁM3U8Parserǁparse_line__mutmut_10': xǁM3U8Parserǁparse_line__mutmut_10, 
        'xǁM3U8Parserǁparse_line__mutmut_11': xǁM3U8Parserǁparse_line__mutmut_11, 
        'xǁM3U8Parserǁparse_line__mutmut_12': xǁM3U8Parserǁparse_line__mutmut_12, 
        'xǁM3U8Parserǁparse_line__mutmut_13': xǁM3U8Parserǁparse_line__mutmut_13, 
        'xǁM3U8Parserǁparse_line__mutmut_14': xǁM3U8Parserǁparse_line__mutmut_14, 
        'xǁM3U8Parserǁparse_line__mutmut_15': xǁM3U8Parserǁparse_line__mutmut_15, 
        'xǁM3U8Parserǁparse_line__mutmut_16': xǁM3U8Parserǁparse_line__mutmut_16, 
        'xǁM3U8Parserǁparse_line__mutmut_17': xǁM3U8Parserǁparse_line__mutmut_17, 
        'xǁM3U8Parserǁparse_line__mutmut_18': xǁM3U8Parserǁparse_line__mutmut_18, 
        'xǁM3U8Parserǁparse_line__mutmut_19': xǁM3U8Parserǁparse_line__mutmut_19, 
        'xǁM3U8Parserǁparse_line__mutmut_20': xǁM3U8Parserǁparse_line__mutmut_20, 
        'xǁM3U8Parserǁparse_line__mutmut_21': xǁM3U8Parserǁparse_line__mutmut_21, 
        'xǁM3U8Parserǁparse_line__mutmut_22': xǁM3U8Parserǁparse_line__mutmut_22, 
        'xǁM3U8Parserǁparse_line__mutmut_23': xǁM3U8Parserǁparse_line__mutmut_23, 
        'xǁM3U8Parserǁparse_line__mutmut_24': xǁM3U8Parserǁparse_line__mutmut_24, 
        'xǁM3U8Parserǁparse_line__mutmut_25': xǁM3U8Parserǁparse_line__mutmut_25
    }
    
    def parse_line(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁparse_line__mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁparse_line__mutmut_mutants"), args, kwargs, self)
        return result 
    
    parse_line.__signature__ = _mutmut_signature(xǁM3U8Parserǁparse_line__mutmut_orig)
    xǁM3U8Parserǁparse_line__mutmut_orig.__name__ = 'xǁM3U8Parserǁparse_line'

    def xǁM3U8Parserǁparse__mutmut_orig(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_1(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = None
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_2(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(None)
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_3(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(None, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_4(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, None))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_5(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_6(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, ))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_7(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = None

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_8(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(None)

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_9(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(None, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_10(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, None))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_11(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_12(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, ))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_13(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=None)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_14(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=False)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_15(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = None
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_16(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(None)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_17(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_18(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith(None):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_19(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("XX#EXTM3UXX"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_20(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#extm3u"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_21(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#extm3u"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_22(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(None)
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_23(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:251]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_24(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError(None)

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_25(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("XXMissing #EXTM3U headerXX")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_26(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("missing #extm3u header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_27(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("MISSING #EXTM3U HEADER")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_28(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #extm3u header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_29(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = None

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_30(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(None, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_31(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, None)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_32(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_33(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, )

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_34(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = None
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_35(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(None)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_36(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("XXaudioXX", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_37(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("AUDIO", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_38(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("Audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_39(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "XXvideoXX", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_40(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "VIDEO", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_41(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "Video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_42(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "XXsubtitlesXX"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_43(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "SUBTITLES"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_44(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "Subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_45(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = None
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_46(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(None, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_47(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, None, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_48(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_49(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_50(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, )
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_51(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(None, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_52(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, None):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_53(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_54(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, ):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_55(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: None, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_56(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id != group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_57(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(None)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_58(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = None

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_59(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_60(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_61(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = None
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_62(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence and 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_63(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 1
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_64(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(None):
            segment.num = media_sequence + i

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_65(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = None

        return self.m3u8

    def xǁM3U8Parserǁparse__mutmut_66(self, data: str | Response) -> TM3U8_co:
        lines: Iterator[str]
        if isinstance(data, str):
            lines = iter(filter(bool, data.splitlines()))
        else:
            lines = iter(filter(bool, data.iter_lines(decode_unicode=True)))

        try:
            line = next(lines)
        except StopIteration:
            return self.m3u8
        else:
            if not line.startswith("#EXTM3U"):
                log.warning(f"Malformed HLS Playlist. Expected #EXTM3U, but got {line[:250]}")
                raise ValueError("Missing #EXTM3U header")

        lines = log.iter(ALL, lines)

        parse_line = self.parse_line
        for line in lines:
            parse_line(line)

        # Associate Media entries with each Playlist
        for playlist in self.m3u8.playlists:
            for media_type in ("audio", "video", "subtitles"):
                group_id = getattr(playlist.stream_info, media_type, None)
                if group_id:
                    for media in filter(lambda m: m.group_id == group_id, self.m3u8.media):
                        playlist.media.append(media)

        self.m3u8.is_master = not not self.m3u8.playlists

        # Update segment numbers
        media_sequence = self.m3u8.media_sequence or 0
        for i, segment in enumerate(self.m3u8.segments):
            segment.num = media_sequence - i

        return self.m3u8
    
    xǁM3U8Parserǁparse__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁparse__mutmut_1': xǁM3U8Parserǁparse__mutmut_1, 
        'xǁM3U8Parserǁparse__mutmut_2': xǁM3U8Parserǁparse__mutmut_2, 
        'xǁM3U8Parserǁparse__mutmut_3': xǁM3U8Parserǁparse__mutmut_3, 
        'xǁM3U8Parserǁparse__mutmut_4': xǁM3U8Parserǁparse__mutmut_4, 
        'xǁM3U8Parserǁparse__mutmut_5': xǁM3U8Parserǁparse__mutmut_5, 
        'xǁM3U8Parserǁparse__mutmut_6': xǁM3U8Parserǁparse__mutmut_6, 
        'xǁM3U8Parserǁparse__mutmut_7': xǁM3U8Parserǁparse__mutmut_7, 
        'xǁM3U8Parserǁparse__mutmut_8': xǁM3U8Parserǁparse__mutmut_8, 
        'xǁM3U8Parserǁparse__mutmut_9': xǁM3U8Parserǁparse__mutmut_9, 
        'xǁM3U8Parserǁparse__mutmut_10': xǁM3U8Parserǁparse__mutmut_10, 
        'xǁM3U8Parserǁparse__mutmut_11': xǁM3U8Parserǁparse__mutmut_11, 
        'xǁM3U8Parserǁparse__mutmut_12': xǁM3U8Parserǁparse__mutmut_12, 
        'xǁM3U8Parserǁparse__mutmut_13': xǁM3U8Parserǁparse__mutmut_13, 
        'xǁM3U8Parserǁparse__mutmut_14': xǁM3U8Parserǁparse__mutmut_14, 
        'xǁM3U8Parserǁparse__mutmut_15': xǁM3U8Parserǁparse__mutmut_15, 
        'xǁM3U8Parserǁparse__mutmut_16': xǁM3U8Parserǁparse__mutmut_16, 
        'xǁM3U8Parserǁparse__mutmut_17': xǁM3U8Parserǁparse__mutmut_17, 
        'xǁM3U8Parserǁparse__mutmut_18': xǁM3U8Parserǁparse__mutmut_18, 
        'xǁM3U8Parserǁparse__mutmut_19': xǁM3U8Parserǁparse__mutmut_19, 
        'xǁM3U8Parserǁparse__mutmut_20': xǁM3U8Parserǁparse__mutmut_20, 
        'xǁM3U8Parserǁparse__mutmut_21': xǁM3U8Parserǁparse__mutmut_21, 
        'xǁM3U8Parserǁparse__mutmut_22': xǁM3U8Parserǁparse__mutmut_22, 
        'xǁM3U8Parserǁparse__mutmut_23': xǁM3U8Parserǁparse__mutmut_23, 
        'xǁM3U8Parserǁparse__mutmut_24': xǁM3U8Parserǁparse__mutmut_24, 
        'xǁM3U8Parserǁparse__mutmut_25': xǁM3U8Parserǁparse__mutmut_25, 
        'xǁM3U8Parserǁparse__mutmut_26': xǁM3U8Parserǁparse__mutmut_26, 
        'xǁM3U8Parserǁparse__mutmut_27': xǁM3U8Parserǁparse__mutmut_27, 
        'xǁM3U8Parserǁparse__mutmut_28': xǁM3U8Parserǁparse__mutmut_28, 
        'xǁM3U8Parserǁparse__mutmut_29': xǁM3U8Parserǁparse__mutmut_29, 
        'xǁM3U8Parserǁparse__mutmut_30': xǁM3U8Parserǁparse__mutmut_30, 
        'xǁM3U8Parserǁparse__mutmut_31': xǁM3U8Parserǁparse__mutmut_31, 
        'xǁM3U8Parserǁparse__mutmut_32': xǁM3U8Parserǁparse__mutmut_32, 
        'xǁM3U8Parserǁparse__mutmut_33': xǁM3U8Parserǁparse__mutmut_33, 
        'xǁM3U8Parserǁparse__mutmut_34': xǁM3U8Parserǁparse__mutmut_34, 
        'xǁM3U8Parserǁparse__mutmut_35': xǁM3U8Parserǁparse__mutmut_35, 
        'xǁM3U8Parserǁparse__mutmut_36': xǁM3U8Parserǁparse__mutmut_36, 
        'xǁM3U8Parserǁparse__mutmut_37': xǁM3U8Parserǁparse__mutmut_37, 
        'xǁM3U8Parserǁparse__mutmut_38': xǁM3U8Parserǁparse__mutmut_38, 
        'xǁM3U8Parserǁparse__mutmut_39': xǁM3U8Parserǁparse__mutmut_39, 
        'xǁM3U8Parserǁparse__mutmut_40': xǁM3U8Parserǁparse__mutmut_40, 
        'xǁM3U8Parserǁparse__mutmut_41': xǁM3U8Parserǁparse__mutmut_41, 
        'xǁM3U8Parserǁparse__mutmut_42': xǁM3U8Parserǁparse__mutmut_42, 
        'xǁM3U8Parserǁparse__mutmut_43': xǁM3U8Parserǁparse__mutmut_43, 
        'xǁM3U8Parserǁparse__mutmut_44': xǁM3U8Parserǁparse__mutmut_44, 
        'xǁM3U8Parserǁparse__mutmut_45': xǁM3U8Parserǁparse__mutmut_45, 
        'xǁM3U8Parserǁparse__mutmut_46': xǁM3U8Parserǁparse__mutmut_46, 
        'xǁM3U8Parserǁparse__mutmut_47': xǁM3U8Parserǁparse__mutmut_47, 
        'xǁM3U8Parserǁparse__mutmut_48': xǁM3U8Parserǁparse__mutmut_48, 
        'xǁM3U8Parserǁparse__mutmut_49': xǁM3U8Parserǁparse__mutmut_49, 
        'xǁM3U8Parserǁparse__mutmut_50': xǁM3U8Parserǁparse__mutmut_50, 
        'xǁM3U8Parserǁparse__mutmut_51': xǁM3U8Parserǁparse__mutmut_51, 
        'xǁM3U8Parserǁparse__mutmut_52': xǁM3U8Parserǁparse__mutmut_52, 
        'xǁM3U8Parserǁparse__mutmut_53': xǁM3U8Parserǁparse__mutmut_53, 
        'xǁM3U8Parserǁparse__mutmut_54': xǁM3U8Parserǁparse__mutmut_54, 
        'xǁM3U8Parserǁparse__mutmut_55': xǁM3U8Parserǁparse__mutmut_55, 
        'xǁM3U8Parserǁparse__mutmut_56': xǁM3U8Parserǁparse__mutmut_56, 
        'xǁM3U8Parserǁparse__mutmut_57': xǁM3U8Parserǁparse__mutmut_57, 
        'xǁM3U8Parserǁparse__mutmut_58': xǁM3U8Parserǁparse__mutmut_58, 
        'xǁM3U8Parserǁparse__mutmut_59': xǁM3U8Parserǁparse__mutmut_59, 
        'xǁM3U8Parserǁparse__mutmut_60': xǁM3U8Parserǁparse__mutmut_60, 
        'xǁM3U8Parserǁparse__mutmut_61': xǁM3U8Parserǁparse__mutmut_61, 
        'xǁM3U8Parserǁparse__mutmut_62': xǁM3U8Parserǁparse__mutmut_62, 
        'xǁM3U8Parserǁparse__mutmut_63': xǁM3U8Parserǁparse__mutmut_63, 
        'xǁM3U8Parserǁparse__mutmut_64': xǁM3U8Parserǁparse__mutmut_64, 
        'xǁM3U8Parserǁparse__mutmut_65': xǁM3U8Parserǁparse__mutmut_65, 
        'xǁM3U8Parserǁparse__mutmut_66': xǁM3U8Parserǁparse__mutmut_66
    }
    
    def parse(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁparse__mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁparse__mutmut_mutants"), args, kwargs, self)
        return result 
    
    parse.__signature__ = _mutmut_signature(xǁM3U8Parserǁparse__mutmut_orig)
    xǁM3U8Parserǁparse__mutmut_orig.__name__ = 'xǁM3U8Parserǁparse'

    def xǁM3U8Parserǁuri__mutmut_orig(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(self.m3u8.uri, uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_1(self, uri: str) -> str:
        if uri or urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(self.m3u8.uri, uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_2(self, uri: str) -> str:
        if uri and urlparse(None).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(self.m3u8.uri, uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_3(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri or self.m3u8.uri:
            return urljoin(self.m3u8.uri, uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_4(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(None, uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_5(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(self.m3u8.uri, None)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_6(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(uri)
        else:
            return uri

    def xǁM3U8Parserǁuri__mutmut_7(self, uri: str) -> str:
        if uri and urlparse(uri).scheme:
            return uri
        elif uri and self.m3u8.uri:
            return urljoin(self.m3u8.uri, )
        else:
            return uri
    
    xǁM3U8Parserǁuri__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁuri__mutmut_1': xǁM3U8Parserǁuri__mutmut_1, 
        'xǁM3U8Parserǁuri__mutmut_2': xǁM3U8Parserǁuri__mutmut_2, 
        'xǁM3U8Parserǁuri__mutmut_3': xǁM3U8Parserǁuri__mutmut_3, 
        'xǁM3U8Parserǁuri__mutmut_4': xǁM3U8Parserǁuri__mutmut_4, 
        'xǁM3U8Parserǁuri__mutmut_5': xǁM3U8Parserǁuri__mutmut_5, 
        'xǁM3U8Parserǁuri__mutmut_6': xǁM3U8Parserǁuri__mutmut_6, 
        'xǁM3U8Parserǁuri__mutmut_7': xǁM3U8Parserǁuri__mutmut_7
    }
    
    def uri(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁuri__mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁuri__mutmut_mutants"), args, kwargs, self)
        return result 
    
    uri.__signature__ = _mutmut_signature(xǁM3U8Parserǁuri__mutmut_orig)
    xǁM3U8Parserǁuri__mutmut_orig.__name__ = 'xǁM3U8Parserǁuri'

    def xǁM3U8Parserǁget_segment__mutmut_orig(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_1(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = None
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_2(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf and ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_3(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(None, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_4(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_5(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, )
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_6(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(1, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_7(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = ""

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_8(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = None
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_9(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = None

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_10(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = True

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_11(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = None
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_12(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = ""

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_13(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = None
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_14(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = ""

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_15(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=None,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_16(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=None,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_17(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=None,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_18(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=None,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_19(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=None,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_20(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=None,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_21(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=None,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_22(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=None,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_23(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=None,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_24(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_25(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_26(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_27(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_28(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_29(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_30(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_31(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_32(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_33(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            )

    def xǁM3U8Parserǁget_segment__mutmut_34(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=+1,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )

    def xǁM3U8Parserǁget_segment__mutmut_35(self, uri: str, **data) -> HLSSegment:
        extinf: ExtInf = self._extinf or ExtInf(0, None)
        self._extinf = None

        discontinuity = self._discontinuity
        self._discontinuity = False

        byterange = self._byterange
        self._byterange = None

        date = self._date
        self._date = None

        # noinspection PyArgumentList
        return self.__segment__(
            uri=uri,
            num=-2,
            duration=extinf.duration,
            title=extinf.title,
            key=self._key,
            discontinuity=discontinuity,
            byterange=byterange,
            date=date,
            map=self._map,
            **data,
        )
    
    xǁM3U8Parserǁget_segment__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁget_segment__mutmut_1': xǁM3U8Parserǁget_segment__mutmut_1, 
        'xǁM3U8Parserǁget_segment__mutmut_2': xǁM3U8Parserǁget_segment__mutmut_2, 
        'xǁM3U8Parserǁget_segment__mutmut_3': xǁM3U8Parserǁget_segment__mutmut_3, 
        'xǁM3U8Parserǁget_segment__mutmut_4': xǁM3U8Parserǁget_segment__mutmut_4, 
        'xǁM3U8Parserǁget_segment__mutmut_5': xǁM3U8Parserǁget_segment__mutmut_5, 
        'xǁM3U8Parserǁget_segment__mutmut_6': xǁM3U8Parserǁget_segment__mutmut_6, 
        'xǁM3U8Parserǁget_segment__mutmut_7': xǁM3U8Parserǁget_segment__mutmut_7, 
        'xǁM3U8Parserǁget_segment__mutmut_8': xǁM3U8Parserǁget_segment__mutmut_8, 
        'xǁM3U8Parserǁget_segment__mutmut_9': xǁM3U8Parserǁget_segment__mutmut_9, 
        'xǁM3U8Parserǁget_segment__mutmut_10': xǁM3U8Parserǁget_segment__mutmut_10, 
        'xǁM3U8Parserǁget_segment__mutmut_11': xǁM3U8Parserǁget_segment__mutmut_11, 
        'xǁM3U8Parserǁget_segment__mutmut_12': xǁM3U8Parserǁget_segment__mutmut_12, 
        'xǁM3U8Parserǁget_segment__mutmut_13': xǁM3U8Parserǁget_segment__mutmut_13, 
        'xǁM3U8Parserǁget_segment__mutmut_14': xǁM3U8Parserǁget_segment__mutmut_14, 
        'xǁM3U8Parserǁget_segment__mutmut_15': xǁM3U8Parserǁget_segment__mutmut_15, 
        'xǁM3U8Parserǁget_segment__mutmut_16': xǁM3U8Parserǁget_segment__mutmut_16, 
        'xǁM3U8Parserǁget_segment__mutmut_17': xǁM3U8Parserǁget_segment__mutmut_17, 
        'xǁM3U8Parserǁget_segment__mutmut_18': xǁM3U8Parserǁget_segment__mutmut_18, 
        'xǁM3U8Parserǁget_segment__mutmut_19': xǁM3U8Parserǁget_segment__mutmut_19, 
        'xǁM3U8Parserǁget_segment__mutmut_20': xǁM3U8Parserǁget_segment__mutmut_20, 
        'xǁM3U8Parserǁget_segment__mutmut_21': xǁM3U8Parserǁget_segment__mutmut_21, 
        'xǁM3U8Parserǁget_segment__mutmut_22': xǁM3U8Parserǁget_segment__mutmut_22, 
        'xǁM3U8Parserǁget_segment__mutmut_23': xǁM3U8Parserǁget_segment__mutmut_23, 
        'xǁM3U8Parserǁget_segment__mutmut_24': xǁM3U8Parserǁget_segment__mutmut_24, 
        'xǁM3U8Parserǁget_segment__mutmut_25': xǁM3U8Parserǁget_segment__mutmut_25, 
        'xǁM3U8Parserǁget_segment__mutmut_26': xǁM3U8Parserǁget_segment__mutmut_26, 
        'xǁM3U8Parserǁget_segment__mutmut_27': xǁM3U8Parserǁget_segment__mutmut_27, 
        'xǁM3U8Parserǁget_segment__mutmut_28': xǁM3U8Parserǁget_segment__mutmut_28, 
        'xǁM3U8Parserǁget_segment__mutmut_29': xǁM3U8Parserǁget_segment__mutmut_29, 
        'xǁM3U8Parserǁget_segment__mutmut_30': xǁM3U8Parserǁget_segment__mutmut_30, 
        'xǁM3U8Parserǁget_segment__mutmut_31': xǁM3U8Parserǁget_segment__mutmut_31, 
        'xǁM3U8Parserǁget_segment__mutmut_32': xǁM3U8Parserǁget_segment__mutmut_32, 
        'xǁM3U8Parserǁget_segment__mutmut_33': xǁM3U8Parserǁget_segment__mutmut_33, 
        'xǁM3U8Parserǁget_segment__mutmut_34': xǁM3U8Parserǁget_segment__mutmut_34, 
        'xǁM3U8Parserǁget_segment__mutmut_35': xǁM3U8Parserǁget_segment__mutmut_35
    }
    
    def get_segment(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁget_segment__mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁget_segment__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_segment.__signature__ = _mutmut_signature(xǁM3U8Parserǁget_segment__mutmut_orig)
    xǁM3U8Parserǁget_segment__mutmut_orig.__name__ = 'xǁM3U8Parserǁget_segment'

    def xǁM3U8Parserǁget_playlist__mutmut_orig(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_1(self, uri: str, **data) -> HLSPlaylist:
        streaminf = None
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_2(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf and {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_3(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = ""

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_4(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = None

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_5(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(None)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_6(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=None,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_7(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=None,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_8(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=None,
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_9(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=None,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_10(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_11(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            media=[],
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_12(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            is_iframe=False,
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_13(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            **data,
        )

    def xǁM3U8Parserǁget_playlist__mutmut_14(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=False,
            )

    def xǁM3U8Parserǁget_playlist__mutmut_15(self, uri: str, **data) -> HLSPlaylist:
        streaminf = self._streaminf or {}
        self._streaminf = None

        stream_info = self.create_stream_info(streaminf)

        # noinspection PyArgumentList
        return self.__playlist__(
            uri=uri,
            stream_info=stream_info,
            media=[],
            is_iframe=True,
            **data,
        )
    
    xǁM3U8Parserǁget_playlist__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁM3U8Parserǁget_playlist__mutmut_1': xǁM3U8Parserǁget_playlist__mutmut_1, 
        'xǁM3U8Parserǁget_playlist__mutmut_2': xǁM3U8Parserǁget_playlist__mutmut_2, 
        'xǁM3U8Parserǁget_playlist__mutmut_3': xǁM3U8Parserǁget_playlist__mutmut_3, 
        'xǁM3U8Parserǁget_playlist__mutmut_4': xǁM3U8Parserǁget_playlist__mutmut_4, 
        'xǁM3U8Parserǁget_playlist__mutmut_5': xǁM3U8Parserǁget_playlist__mutmut_5, 
        'xǁM3U8Parserǁget_playlist__mutmut_6': xǁM3U8Parserǁget_playlist__mutmut_6, 
        'xǁM3U8Parserǁget_playlist__mutmut_7': xǁM3U8Parserǁget_playlist__mutmut_7, 
        'xǁM3U8Parserǁget_playlist__mutmut_8': xǁM3U8Parserǁget_playlist__mutmut_8, 
        'xǁM3U8Parserǁget_playlist__mutmut_9': xǁM3U8Parserǁget_playlist__mutmut_9, 
        'xǁM3U8Parserǁget_playlist__mutmut_10': xǁM3U8Parserǁget_playlist__mutmut_10, 
        'xǁM3U8Parserǁget_playlist__mutmut_11': xǁM3U8Parserǁget_playlist__mutmut_11, 
        'xǁM3U8Parserǁget_playlist__mutmut_12': xǁM3U8Parserǁget_playlist__mutmut_12, 
        'xǁM3U8Parserǁget_playlist__mutmut_13': xǁM3U8Parserǁget_playlist__mutmut_13, 
        'xǁM3U8Parserǁget_playlist__mutmut_14': xǁM3U8Parserǁget_playlist__mutmut_14, 
        'xǁM3U8Parserǁget_playlist__mutmut_15': xǁM3U8Parserǁget_playlist__mutmut_15
    }
    
    def get_playlist(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁM3U8Parserǁget_playlist__mutmut_orig"), object.__getattribute__(self, "xǁM3U8Parserǁget_playlist__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_playlist.__signature__ = _mutmut_signature(xǁM3U8Parserǁget_playlist__mutmut_orig)
    xǁM3U8Parserǁget_playlist__mutmut_orig.__name__ = 'xǁM3U8Parserǁget_playlist'


def x_parse_m3u8__mutmut_orig(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is None and isinstance(data, Response):
        base_uri = data.url

    return parser(base_uri).parse(data)


def x_parse_m3u8__mutmut_1(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is not None and isinstance(data, Response):
        base_uri = data.url

    return parser(base_uri).parse(data)


def x_parse_m3u8__mutmut_2(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is None or isinstance(data, Response):
        base_uri = data.url

    return parser(base_uri).parse(data)


def x_parse_m3u8__mutmut_3(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is None and isinstance(data, Response):
        base_uri = None

    return parser(base_uri).parse(data)


def x_parse_m3u8__mutmut_4(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is None and isinstance(data, Response):
        base_uri = data.url

    return parser(base_uri).parse(None)


def x_parse_m3u8__mutmut_5(
    data: str | Response,
    base_uri: str | None = None,
    parser: type[M3U8Parser[TM3U8_co, THLSSegment_co, THLSPlaylist_co]] = M3U8Parser,
) -> TM3U8_co:
    """
    Parse an M3U8 playlist from a string of data or an HTTP response.

    If specified, *base_uri* is the base URI that relative URIs will
    be joined together with, otherwise relative URIs will be as is.

    If specified, *parser* can be an M3U8Parser subclass to be used
    to parse the data.
    """
    if base_uri is None and isinstance(data, Response):
        base_uri = data.url

    return parser(None).parse(data)

x_parse_m3u8__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_m3u8__mutmut_1': x_parse_m3u8__mutmut_1, 
    'x_parse_m3u8__mutmut_2': x_parse_m3u8__mutmut_2, 
    'x_parse_m3u8__mutmut_3': x_parse_m3u8__mutmut_3, 
    'x_parse_m3u8__mutmut_4': x_parse_m3u8__mutmut_4, 
    'x_parse_m3u8__mutmut_5': x_parse_m3u8__mutmut_5
}

def parse_m3u8(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_m3u8__mutmut_orig, x_parse_m3u8__mutmut_mutants, args, kwargs)
    return result 

parse_m3u8.__signature__ = _mutmut_signature(x_parse_m3u8__mutmut_orig)
x_parse_m3u8__mutmut_orig.__name__ = 'x_parse_m3u8'

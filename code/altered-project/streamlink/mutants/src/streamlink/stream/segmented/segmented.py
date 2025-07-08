from __future__ import annotations

import logging
import queue
from collections.abc import Generator
from concurrent import futures
from concurrent.futures import Future, ThreadPoolExecutor
from threading import Event, current_thread
from typing import TYPE_CHECKING, ClassVar, Generic, TypeVar

from streamlink.buffers import RingBuffer
from streamlink.stream.segmented.segment import Segment
from streamlink.stream.stream import Stream, StreamIO
from streamlink.utils.thread import NamedThread


if TYPE_CHECKING:
    try:
        from typing import TypeAlias  # type: ignore[attr-defined]
    except ImportError:
        from typing_extensions import TypeAlias


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


class AwaitableMixin:
    def xǁAwaitableMixinǁ__init____mutmut_orig(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._wait = Event()
    def xǁAwaitableMixinǁ__init____mutmut_1(self, *args, **kwargs):
        super().__init__(**kwargs)
        self._wait = Event()
    def xǁAwaitableMixinǁ__init____mutmut_2(self, *args, **kwargs):
        super().__init__(*args, )
        self._wait = Event()
    def xǁAwaitableMixinǁ__init____mutmut_3(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._wait = None
    
    xǁAwaitableMixinǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAwaitableMixinǁ__init____mutmut_1': xǁAwaitableMixinǁ__init____mutmut_1, 
        'xǁAwaitableMixinǁ__init____mutmut_2': xǁAwaitableMixinǁ__init____mutmut_2, 
        'xǁAwaitableMixinǁ__init____mutmut_3': xǁAwaitableMixinǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAwaitableMixinǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁAwaitableMixinǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁAwaitableMixinǁ__init____mutmut_orig)
    xǁAwaitableMixinǁ__init____mutmut_orig.__name__ = 'xǁAwaitableMixinǁ__init__'

    def xǁAwaitableMixinǁwait__mutmut_orig(self, time: float) -> bool:
        """
        Pause the thread for a specified time.
        Return False if interrupted by another thread and True if the time runs out normally.
        """
        return not self._wait.wait(time)

    def xǁAwaitableMixinǁwait__mutmut_1(self, time: float) -> bool:
        """
        Pause the thread for a specified time.
        Return False if interrupted by another thread and True if the time runs out normally.
        """
        return self._wait.wait(time)

    def xǁAwaitableMixinǁwait__mutmut_2(self, time: float) -> bool:
        """
        Pause the thread for a specified time.
        Return False if interrupted by another thread and True if the time runs out normally.
        """
        return not self._wait.wait(None)
    
    xǁAwaitableMixinǁwait__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁAwaitableMixinǁwait__mutmut_1': xǁAwaitableMixinǁwait__mutmut_1, 
        'xǁAwaitableMixinǁwait__mutmut_2': xǁAwaitableMixinǁwait__mutmut_2
    }
    
    def wait(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁAwaitableMixinǁwait__mutmut_orig"), object.__getattribute__(self, "xǁAwaitableMixinǁwait__mutmut_mutants"), args, kwargs, self)
        return result 
    
    wait.__signature__ = _mutmut_signature(xǁAwaitableMixinǁwait__mutmut_orig)
    xǁAwaitableMixinǁwait__mutmut_orig.__name__ = 'xǁAwaitableMixinǁwait'


TSegment = TypeVar("TSegment", bound=Segment)
TResult = TypeVar("TResult")
TResultFuture: TypeAlias = "Future[TResult | None]"
TQueueItem: TypeAlias = "tuple[TSegment, TResultFuture, tuple]"


class SegmentedStreamWriter(AwaitableMixin, NamedThread, Generic[TSegment, TResult]):
    """
    The base writer thread.
    This thread is responsible for fetching segments, processing them and finally writing the data to the buffer.
    """

    reader: SegmentedStreamReader[TSegment, TResult]
    stream: Stream

    def xǁSegmentedStreamWriterǁ__init____mutmut_orig(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_1(
        self,
        reader: SegmentedStreamReader,
        size: int = 21,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_2(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=None, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_3(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=None)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_4(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_5(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, )

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_6(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=False, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_7(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = None

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_8(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = True

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_9(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = None
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_10(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = None
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_11(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = None

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_12(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = None
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_13(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries and self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_14(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get(None)
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_15(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("XXstream-segment-attemptsXX")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_16(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("STREAM-SEGMENT-ATTEMPTS")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_17(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("Stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_18(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = None
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_19(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads and self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_20(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get(None)
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_21(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("XXstream-segment-threadsXX")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_22(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("STREAM-SEGMENT-THREADS")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_23(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("Stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_24(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = None

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_25(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout and self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_26(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get(None)

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_27(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("XXstream-segment-timeoutXX")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_28(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("STREAM-SEGMENT-TIMEOUT")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_29(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("Stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_30(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = None
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_31(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=None, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_32(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=None)
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_33(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_34(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, )
        self._queue: queue.Queue[TQueueItem] = queue.Queue(size)

    def xǁSegmentedStreamWriterǁ__init____mutmut_35(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = None

    def xǁSegmentedStreamWriterǁ__init____mutmut_36(
        self,
        reader: SegmentedStreamReader,
        size: int = 20,
        retries: int | None = None,
        threads: int | None = None,
        timeout: float | None = None,
        name: str | None = None,
    ) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.stream = reader.stream
        self.session = reader.session

        self.retries = retries or self.session.options.get("stream-segment-attempts")
        self.threads = threads or self.session.options.get("stream-segment-threads")
        self.timeout = timeout or self.session.options.get("stream-segment-timeout")

        self.executor = ThreadPoolExecutor(max_workers=self.threads, thread_name_prefix=f"{self.name}-executor")
        self._queue: queue.Queue[TQueueItem] = queue.Queue(None)
    
    xǁSegmentedStreamWriterǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁ__init____mutmut_1': xǁSegmentedStreamWriterǁ__init____mutmut_1, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_2': xǁSegmentedStreamWriterǁ__init____mutmut_2, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_3': xǁSegmentedStreamWriterǁ__init____mutmut_3, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_4': xǁSegmentedStreamWriterǁ__init____mutmut_4, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_5': xǁSegmentedStreamWriterǁ__init____mutmut_5, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_6': xǁSegmentedStreamWriterǁ__init____mutmut_6, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_7': xǁSegmentedStreamWriterǁ__init____mutmut_7, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_8': xǁSegmentedStreamWriterǁ__init____mutmut_8, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_9': xǁSegmentedStreamWriterǁ__init____mutmut_9, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_10': xǁSegmentedStreamWriterǁ__init____mutmut_10, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_11': xǁSegmentedStreamWriterǁ__init____mutmut_11, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_12': xǁSegmentedStreamWriterǁ__init____mutmut_12, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_13': xǁSegmentedStreamWriterǁ__init____mutmut_13, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_14': xǁSegmentedStreamWriterǁ__init____mutmut_14, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_15': xǁSegmentedStreamWriterǁ__init____mutmut_15, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_16': xǁSegmentedStreamWriterǁ__init____mutmut_16, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_17': xǁSegmentedStreamWriterǁ__init____mutmut_17, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_18': xǁSegmentedStreamWriterǁ__init____mutmut_18, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_19': xǁSegmentedStreamWriterǁ__init____mutmut_19, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_20': xǁSegmentedStreamWriterǁ__init____mutmut_20, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_21': xǁSegmentedStreamWriterǁ__init____mutmut_21, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_22': xǁSegmentedStreamWriterǁ__init____mutmut_22, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_23': xǁSegmentedStreamWriterǁ__init____mutmut_23, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_24': xǁSegmentedStreamWriterǁ__init____mutmut_24, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_25': xǁSegmentedStreamWriterǁ__init____mutmut_25, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_26': xǁSegmentedStreamWriterǁ__init____mutmut_26, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_27': xǁSegmentedStreamWriterǁ__init____mutmut_27, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_28': xǁSegmentedStreamWriterǁ__init____mutmut_28, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_29': xǁSegmentedStreamWriterǁ__init____mutmut_29, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_30': xǁSegmentedStreamWriterǁ__init____mutmut_30, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_31': xǁSegmentedStreamWriterǁ__init____mutmut_31, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_32': xǁSegmentedStreamWriterǁ__init____mutmut_32, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_33': xǁSegmentedStreamWriterǁ__init____mutmut_33, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_34': xǁSegmentedStreamWriterǁ__init____mutmut_34, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_35': xǁSegmentedStreamWriterǁ__init____mutmut_35, 
        'xǁSegmentedStreamWriterǁ__init____mutmut_36': xǁSegmentedStreamWriterǁ__init____mutmut_36
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁ__init____mutmut_orig)
    xǁSegmentedStreamWriterǁ__init____mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁ__init__'

    def xǁSegmentedStreamWriterǁclose__mutmut_orig(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_1(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug(None)

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_2(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("XXClosing writer threadXX")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_3(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_4(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("CLOSING WRITER THREAD")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_5(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = None
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_6(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = False
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_7(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=None, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_8(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=None)

    def xǁSegmentedStreamWriterǁclose__mutmut_9(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_10(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, )

    def xǁSegmentedStreamWriterǁclose__mutmut_11(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=False, cancel_futures=True)

    def xǁSegmentedStreamWriterǁclose__mutmut_12(self) -> None:
        """
        Shuts down the thread, its executor and closes the reader (worker thread and buffer).
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing writer thread")

        self.closed = True
        self._wait.set()

        self.reader.close()
        self.executor.shutdown(wait=True, cancel_futures=False)
    
    xǁSegmentedStreamWriterǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁclose__mutmut_1': xǁSegmentedStreamWriterǁclose__mutmut_1, 
        'xǁSegmentedStreamWriterǁclose__mutmut_2': xǁSegmentedStreamWriterǁclose__mutmut_2, 
        'xǁSegmentedStreamWriterǁclose__mutmut_3': xǁSegmentedStreamWriterǁclose__mutmut_3, 
        'xǁSegmentedStreamWriterǁclose__mutmut_4': xǁSegmentedStreamWriterǁclose__mutmut_4, 
        'xǁSegmentedStreamWriterǁclose__mutmut_5': xǁSegmentedStreamWriterǁclose__mutmut_5, 
        'xǁSegmentedStreamWriterǁclose__mutmut_6': xǁSegmentedStreamWriterǁclose__mutmut_6, 
        'xǁSegmentedStreamWriterǁclose__mutmut_7': xǁSegmentedStreamWriterǁclose__mutmut_7, 
        'xǁSegmentedStreamWriterǁclose__mutmut_8': xǁSegmentedStreamWriterǁclose__mutmut_8, 
        'xǁSegmentedStreamWriterǁclose__mutmut_9': xǁSegmentedStreamWriterǁclose__mutmut_9, 
        'xǁSegmentedStreamWriterǁclose__mutmut_10': xǁSegmentedStreamWriterǁclose__mutmut_10, 
        'xǁSegmentedStreamWriterǁclose__mutmut_11': xǁSegmentedStreamWriterǁclose__mutmut_11, 
        'xǁSegmentedStreamWriterǁclose__mutmut_12': xǁSegmentedStreamWriterǁclose__mutmut_12
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁclose__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁclose__mutmut_orig)
    xǁSegmentedStreamWriterǁclose__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁclose'

    def xǁSegmentedStreamWriterǁput__mutmut_orig(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_1(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is not None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_2(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = ""
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_3(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = None

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_4(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(None, segment)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_5(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, None)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_6(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(segment)

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_7(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, )

        self.queue(segment, future)

    def xǁSegmentedStreamWriterǁput__mutmut_8(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(None, future)

    def xǁSegmentedStreamWriterǁput__mutmut_9(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(segment, None)

    def xǁSegmentedStreamWriterǁput__mutmut_10(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(future)

    def xǁSegmentedStreamWriterǁput__mutmut_11(self, segment: TSegment | None) -> None:
        """
        Adds a segment to the download pool and write queue.
        """

        if self.closed:  # pragma: no cover
            return

        future: TResultFuture | None
        if segment is None:
            future = None
        else:
            future = self.executor.submit(self.fetch, segment)

        self.queue(segment, )
    
    xǁSegmentedStreamWriterǁput__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁput__mutmut_1': xǁSegmentedStreamWriterǁput__mutmut_1, 
        'xǁSegmentedStreamWriterǁput__mutmut_2': xǁSegmentedStreamWriterǁput__mutmut_2, 
        'xǁSegmentedStreamWriterǁput__mutmut_3': xǁSegmentedStreamWriterǁput__mutmut_3, 
        'xǁSegmentedStreamWriterǁput__mutmut_4': xǁSegmentedStreamWriterǁput__mutmut_4, 
        'xǁSegmentedStreamWriterǁput__mutmut_5': xǁSegmentedStreamWriterǁput__mutmut_5, 
        'xǁSegmentedStreamWriterǁput__mutmut_6': xǁSegmentedStreamWriterǁput__mutmut_6, 
        'xǁSegmentedStreamWriterǁput__mutmut_7': xǁSegmentedStreamWriterǁput__mutmut_7, 
        'xǁSegmentedStreamWriterǁput__mutmut_8': xǁSegmentedStreamWriterǁput__mutmut_8, 
        'xǁSegmentedStreamWriterǁput__mutmut_9': xǁSegmentedStreamWriterǁput__mutmut_9, 
        'xǁSegmentedStreamWriterǁput__mutmut_10': xǁSegmentedStreamWriterǁput__mutmut_10, 
        'xǁSegmentedStreamWriterǁput__mutmut_11': xǁSegmentedStreamWriterǁput__mutmut_11
    }
    
    def put(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁput__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁput__mutmut_mutants"), args, kwargs, self)
        return result 
    
    put.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁput__mutmut_orig)
    xǁSegmentedStreamWriterǁput__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁput'

    def xǁSegmentedStreamWriterǁqueue__mutmut_orig(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None or future is None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_1(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_2(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is not None or future is None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_3(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None and future is None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_4(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None or future is not None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_5(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None or future is None else (segment, future, data)
        while self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_6(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None or future is None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(None)
                return
            except queue.Full:  # pragma: no cover
                continue

    def xǁSegmentedStreamWriterǁqueue__mutmut_7(self, segment: TSegment | None, future: TResultFuture | None, *data) -> None:
        """
        Puts values into a queue but aborts if this thread is closed.
        """

        item = None if segment is None or future is None else (segment, future, data)
        while not self.closed:  # pragma: no branch
            try:
                self._queue_put(item)
                return
            except queue.Full:  # pragma: no cover
                break
    
    xǁSegmentedStreamWriterǁqueue__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁqueue__mutmut_1': xǁSegmentedStreamWriterǁqueue__mutmut_1, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_2': xǁSegmentedStreamWriterǁqueue__mutmut_2, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_3': xǁSegmentedStreamWriterǁqueue__mutmut_3, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_4': xǁSegmentedStreamWriterǁqueue__mutmut_4, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_5': xǁSegmentedStreamWriterǁqueue__mutmut_5, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_6': xǁSegmentedStreamWriterǁqueue__mutmut_6, 
        'xǁSegmentedStreamWriterǁqueue__mutmut_7': xǁSegmentedStreamWriterǁqueue__mutmut_7
    }
    
    def queue(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁqueue__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁqueue__mutmut_mutants"), args, kwargs, self)
        return result 
    
    queue.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁqueue__mutmut_orig)
    xǁSegmentedStreamWriterǁqueue__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁqueue'

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_orig(self, item: TQueueItem) -> None:
        self._queue.put(item, block=True, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_1(self, item: TQueueItem) -> None:
        self._queue.put(None, block=True, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_2(self, item: TQueueItem) -> None:
        self._queue.put(item, block=None, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_3(self, item: TQueueItem) -> None:
        self._queue.put(item, block=True, timeout=None)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_4(self, item: TQueueItem) -> None:
        self._queue.put(block=True, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_5(self, item: TQueueItem) -> None:
        self._queue.put(item, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_6(self, item: TQueueItem) -> None:
        self._queue.put(item, block=True, )

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_7(self, item: TQueueItem) -> None:
        self._queue.put(item, block=False, timeout=1)

    def xǁSegmentedStreamWriterǁ_queue_put__mutmut_8(self, item: TQueueItem) -> None:
        self._queue.put(item, block=True, timeout=2)
    
    xǁSegmentedStreamWriterǁ_queue_put__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁ_queue_put__mutmut_1': xǁSegmentedStreamWriterǁ_queue_put__mutmut_1, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_2': xǁSegmentedStreamWriterǁ_queue_put__mutmut_2, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_3': xǁSegmentedStreamWriterǁ_queue_put__mutmut_3, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_4': xǁSegmentedStreamWriterǁ_queue_put__mutmut_4, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_5': xǁSegmentedStreamWriterǁ_queue_put__mutmut_5, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_6': xǁSegmentedStreamWriterǁ_queue_put__mutmut_6, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_7': xǁSegmentedStreamWriterǁ_queue_put__mutmut_7, 
        'xǁSegmentedStreamWriterǁ_queue_put__mutmut_8': xǁSegmentedStreamWriterǁ_queue_put__mutmut_8
    }
    
    def _queue_put(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁ_queue_put__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁ_queue_put__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _queue_put.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁ_queue_put__mutmut_orig)
    xǁSegmentedStreamWriterǁ_queue_put__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁ_queue_put'

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_orig(self) -> TQueueItem:
        return self._queue.get(block=True, timeout=0.5)

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_1(self) -> TQueueItem:
        return self._queue.get(block=None, timeout=0.5)

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_2(self) -> TQueueItem:
        return self._queue.get(block=True, timeout=None)

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_3(self) -> TQueueItem:
        return self._queue.get(timeout=0.5)

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_4(self) -> TQueueItem:
        return self._queue.get(block=True, )

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_5(self) -> TQueueItem:
        return self._queue.get(block=False, timeout=0.5)

    def xǁSegmentedStreamWriterǁ_queue_get__mutmut_6(self) -> TQueueItem:
        return self._queue.get(block=True, timeout=1.5)
    
    xǁSegmentedStreamWriterǁ_queue_get__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁ_queue_get__mutmut_1': xǁSegmentedStreamWriterǁ_queue_get__mutmut_1, 
        'xǁSegmentedStreamWriterǁ_queue_get__mutmut_2': xǁSegmentedStreamWriterǁ_queue_get__mutmut_2, 
        'xǁSegmentedStreamWriterǁ_queue_get__mutmut_3': xǁSegmentedStreamWriterǁ_queue_get__mutmut_3, 
        'xǁSegmentedStreamWriterǁ_queue_get__mutmut_4': xǁSegmentedStreamWriterǁ_queue_get__mutmut_4, 
        'xǁSegmentedStreamWriterǁ_queue_get__mutmut_5': xǁSegmentedStreamWriterǁ_queue_get__mutmut_5, 
        'xǁSegmentedStreamWriterǁ_queue_get__mutmut_6': xǁSegmentedStreamWriterǁ_queue_get__mutmut_6
    }
    
    def _queue_get(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁ_queue_get__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁ_queue_get__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _queue_get.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁ_queue_get__mutmut_orig)
    xǁSegmentedStreamWriterǁ_queue_get__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁ_queue_get'

    @staticmethod
    def _future_result(future: TResultFuture) -> TResult | None:
        return future.result(timeout=0.5)

    def fetch(self, segment: TSegment) -> TResult | None:
        """
        Fetches a segment.
        Should be overridden by the inheriting class.
        """

    def write(self, segment: TSegment, result: TResult, *data) -> None:
        """
        Writes a segment to the buffer.
        Should be overridden by the inheriting class.
        """

    def xǁSegmentedStreamWriterǁrun__mutmut_orig(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_1(self) -> None:
        while self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_2(self) -> None:
        while not self.closed:
            try:
                item = None
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_3(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                break

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_4(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is not None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_5(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                return

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_6(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = None
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_7(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_8(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = None
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_9(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(None)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_10(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    break
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_11(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    return

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_12(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is None:  # pragma: no branch
                    self.write(segment, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_13(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(None, result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_14(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, None, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_15(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(result, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_16(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, *data)

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_17(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, )

                break

        self.close()

    def xǁSegmentedStreamWriterǁrun__mutmut_18(self) -> None:
        while not self.closed:
            try:
                item = self._queue_get()
            except queue.Empty:  # pragma: no cover
                continue

            # End of stream
            if item is None:
                break

            segment, future, data = item
            while not self.closed:  # pragma: no branch
                try:
                    result = self._future_result(future)
                except futures.TimeoutError:  # pragma: no cover
                    continue
                except futures.CancelledError:  # pragma: no cover
                    break

                if result is not None:  # pragma: no branch
                    self.write(segment, result, *data)

                return

        self.close()
    
    xǁSegmentedStreamWriterǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWriterǁrun__mutmut_1': xǁSegmentedStreamWriterǁrun__mutmut_1, 
        'xǁSegmentedStreamWriterǁrun__mutmut_2': xǁSegmentedStreamWriterǁrun__mutmut_2, 
        'xǁSegmentedStreamWriterǁrun__mutmut_3': xǁSegmentedStreamWriterǁrun__mutmut_3, 
        'xǁSegmentedStreamWriterǁrun__mutmut_4': xǁSegmentedStreamWriterǁrun__mutmut_4, 
        'xǁSegmentedStreamWriterǁrun__mutmut_5': xǁSegmentedStreamWriterǁrun__mutmut_5, 
        'xǁSegmentedStreamWriterǁrun__mutmut_6': xǁSegmentedStreamWriterǁrun__mutmut_6, 
        'xǁSegmentedStreamWriterǁrun__mutmut_7': xǁSegmentedStreamWriterǁrun__mutmut_7, 
        'xǁSegmentedStreamWriterǁrun__mutmut_8': xǁSegmentedStreamWriterǁrun__mutmut_8, 
        'xǁSegmentedStreamWriterǁrun__mutmut_9': xǁSegmentedStreamWriterǁrun__mutmut_9, 
        'xǁSegmentedStreamWriterǁrun__mutmut_10': xǁSegmentedStreamWriterǁrun__mutmut_10, 
        'xǁSegmentedStreamWriterǁrun__mutmut_11': xǁSegmentedStreamWriterǁrun__mutmut_11, 
        'xǁSegmentedStreamWriterǁrun__mutmut_12': xǁSegmentedStreamWriterǁrun__mutmut_12, 
        'xǁSegmentedStreamWriterǁrun__mutmut_13': xǁSegmentedStreamWriterǁrun__mutmut_13, 
        'xǁSegmentedStreamWriterǁrun__mutmut_14': xǁSegmentedStreamWriterǁrun__mutmut_14, 
        'xǁSegmentedStreamWriterǁrun__mutmut_15': xǁSegmentedStreamWriterǁrun__mutmut_15, 
        'xǁSegmentedStreamWriterǁrun__mutmut_16': xǁSegmentedStreamWriterǁrun__mutmut_16, 
        'xǁSegmentedStreamWriterǁrun__mutmut_17': xǁSegmentedStreamWriterǁrun__mutmut_17, 
        'xǁSegmentedStreamWriterǁrun__mutmut_18': xǁSegmentedStreamWriterǁrun__mutmut_18
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWriterǁrun__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWriterǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁSegmentedStreamWriterǁrun__mutmut_orig)
    xǁSegmentedStreamWriterǁrun__mutmut_orig.__name__ = 'xǁSegmentedStreamWriterǁrun'


class SegmentedStreamWorker(AwaitableMixin, NamedThread, Generic[TSegment, TResult]):
    """
    The base worker thread.
    This thread is responsible for queueing up segments in the writer thread.
    """

    reader: SegmentedStreamReader[TSegment, TResult]
    writer: SegmentedStreamWriter[TSegment, TResult]
    stream: Stream

    def xǁSegmentedStreamWorkerǁ__init____mutmut_orig(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_1(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=None, name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_2(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=None)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_3(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_4(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, )

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_5(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=False, name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_6(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = None

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_7(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = True

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_8(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = None
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_9(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.writer = None
        self.stream = reader.stream
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_10(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = None
        self.session = reader.session

    def xǁSegmentedStreamWorkerǁ__init____mutmut_11(self, reader: SegmentedStreamReader, name: str | None = None, **kwargs) -> None:
        super().__init__(daemon=True, name=name)

        self.closed = False

        self.reader = reader
        self.writer = reader.writer
        self.stream = reader.stream
        self.session = None
    
    xǁSegmentedStreamWorkerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWorkerǁ__init____mutmut_1': xǁSegmentedStreamWorkerǁ__init____mutmut_1, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_2': xǁSegmentedStreamWorkerǁ__init____mutmut_2, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_3': xǁSegmentedStreamWorkerǁ__init____mutmut_3, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_4': xǁSegmentedStreamWorkerǁ__init____mutmut_4, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_5': xǁSegmentedStreamWorkerǁ__init____mutmut_5, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_6': xǁSegmentedStreamWorkerǁ__init____mutmut_6, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_7': xǁSegmentedStreamWorkerǁ__init____mutmut_7, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_8': xǁSegmentedStreamWorkerǁ__init____mutmut_8, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_9': xǁSegmentedStreamWorkerǁ__init____mutmut_9, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_10': xǁSegmentedStreamWorkerǁ__init____mutmut_10, 
        'xǁSegmentedStreamWorkerǁ__init____mutmut_11': xǁSegmentedStreamWorkerǁ__init____mutmut_11
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWorkerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWorkerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSegmentedStreamWorkerǁ__init____mutmut_orig)
    xǁSegmentedStreamWorkerǁ__init____mutmut_orig.__name__ = 'xǁSegmentedStreamWorkerǁ__init__'

    def xǁSegmentedStreamWorkerǁclose__mutmut_orig(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing worker thread")

        self.closed = True
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_1(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug(None)

        self.closed = True
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_2(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("XXClosing worker threadXX")

        self.closed = True
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_3(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("closing worker thread")

        self.closed = True
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_4(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("CLOSING WORKER THREAD")

        self.closed = True
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_5(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing worker thread")

        self.closed = None
        self._wait.set()

    def xǁSegmentedStreamWorkerǁclose__mutmut_6(self) -> None:
        """
        Shuts down the thread.
        """

        if self.closed:  # pragma: no cover
            return

        log.debug("Closing worker thread")

        self.closed = False
        self._wait.set()
    
    xǁSegmentedStreamWorkerǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWorkerǁclose__mutmut_1': xǁSegmentedStreamWorkerǁclose__mutmut_1, 
        'xǁSegmentedStreamWorkerǁclose__mutmut_2': xǁSegmentedStreamWorkerǁclose__mutmut_2, 
        'xǁSegmentedStreamWorkerǁclose__mutmut_3': xǁSegmentedStreamWorkerǁclose__mutmut_3, 
        'xǁSegmentedStreamWorkerǁclose__mutmut_4': xǁSegmentedStreamWorkerǁclose__mutmut_4, 
        'xǁSegmentedStreamWorkerǁclose__mutmut_5': xǁSegmentedStreamWorkerǁclose__mutmut_5, 
        'xǁSegmentedStreamWorkerǁclose__mutmut_6': xǁSegmentedStreamWorkerǁclose__mutmut_6
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWorkerǁclose__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWorkerǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁSegmentedStreamWorkerǁclose__mutmut_orig)
    xǁSegmentedStreamWorkerǁclose__mutmut_orig.__name__ = 'xǁSegmentedStreamWorkerǁclose'

    def iter_segments(self) -> Generator[TSegment, None, None]:
        """
        The iterator that generates segments for the worker thread.
        Should be overridden by the inheriting class.
        """

        return
        # noinspection PyUnreachableCode
        yield

    def xǁSegmentedStreamWorkerǁrun__mutmut_orig(self) -> None:
        for segment in self.iter_segments():
            if self.closed:  # pragma: no cover
                break
            self.writer.put(segment)

        # End of stream, tells the writer to exit
        self.writer.put(None)
        self.close()

    def xǁSegmentedStreamWorkerǁrun__mutmut_1(self) -> None:
        for segment in self.iter_segments():
            if self.closed:  # pragma: no cover
                return
            self.writer.put(segment)

        # End of stream, tells the writer to exit
        self.writer.put(None)
        self.close()

    def xǁSegmentedStreamWorkerǁrun__mutmut_2(self) -> None:
        for segment in self.iter_segments():
            if self.closed:  # pragma: no cover
                break
            self.writer.put(None)

        # End of stream, tells the writer to exit
        self.writer.put(None)
        self.close()
    
    xǁSegmentedStreamWorkerǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamWorkerǁrun__mutmut_1': xǁSegmentedStreamWorkerǁrun__mutmut_1, 
        'xǁSegmentedStreamWorkerǁrun__mutmut_2': xǁSegmentedStreamWorkerǁrun__mutmut_2
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamWorkerǁrun__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamWorkerǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁSegmentedStreamWorkerǁrun__mutmut_orig)
    xǁSegmentedStreamWorkerǁrun__mutmut_orig.__name__ = 'xǁSegmentedStreamWorkerǁrun'


class SegmentedStreamReader(StreamIO, Generic[TSegment, TResult]):
    __worker__: ClassVar[type[SegmentedStreamWorker]] = SegmentedStreamWorker
    __writer__: ClassVar[type[SegmentedStreamWriter]] = SegmentedStreamWriter

    worker: SegmentedStreamWorker[TSegment, TResult]
    writer: SegmentedStreamWriter[TSegment, TResult]
    stream: Stream

    def xǁSegmentedStreamReaderǁ__init____mutmut_orig(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_1(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = None
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_2(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = None

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_3(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = None

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_4(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get(None)

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_5(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("XXstream-timeoutXX")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_6(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("STREAM-TIMEOUT")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_7(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("Stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_8(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = None
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_9(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option(None)
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_10(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("XXringbuffer-sizeXX")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_11(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("RINGBUFFER-SIZE")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_12(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("Ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_13(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = None

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_14(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(None)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_15(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = None
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_16(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(None, name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_17(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=None)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_18(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(name=name)
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_19(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, )
        self.worker = self.__worker__(self, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_20(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = None

    def xǁSegmentedStreamReaderǁ__init____mutmut_21(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(None, name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_22(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, name=None)

    def xǁSegmentedStreamReaderǁ__init____mutmut_23(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(name=name)

    def xǁSegmentedStreamReaderǁ__init____mutmut_24(self, stream: Stream, name: str | None = None) -> None:
        super().__init__()

        self.stream = stream
        self.session = stream.session

        self.timeout = self.session.options.get("stream-timeout")

        buffer_size = self.session.get_option("ringbuffer-size")
        self.buffer = RingBuffer(buffer_size)

        self.writer = self.__writer__(self, name=name)
        self.worker = self.__worker__(self, )
    
    xǁSegmentedStreamReaderǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamReaderǁ__init____mutmut_1': xǁSegmentedStreamReaderǁ__init____mutmut_1, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_2': xǁSegmentedStreamReaderǁ__init____mutmut_2, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_3': xǁSegmentedStreamReaderǁ__init____mutmut_3, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_4': xǁSegmentedStreamReaderǁ__init____mutmut_4, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_5': xǁSegmentedStreamReaderǁ__init____mutmut_5, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_6': xǁSegmentedStreamReaderǁ__init____mutmut_6, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_7': xǁSegmentedStreamReaderǁ__init____mutmut_7, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_8': xǁSegmentedStreamReaderǁ__init____mutmut_8, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_9': xǁSegmentedStreamReaderǁ__init____mutmut_9, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_10': xǁSegmentedStreamReaderǁ__init____mutmut_10, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_11': xǁSegmentedStreamReaderǁ__init____mutmut_11, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_12': xǁSegmentedStreamReaderǁ__init____mutmut_12, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_13': xǁSegmentedStreamReaderǁ__init____mutmut_13, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_14': xǁSegmentedStreamReaderǁ__init____mutmut_14, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_15': xǁSegmentedStreamReaderǁ__init____mutmut_15, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_16': xǁSegmentedStreamReaderǁ__init____mutmut_16, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_17': xǁSegmentedStreamReaderǁ__init____mutmut_17, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_18': xǁSegmentedStreamReaderǁ__init____mutmut_18, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_19': xǁSegmentedStreamReaderǁ__init____mutmut_19, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_20': xǁSegmentedStreamReaderǁ__init____mutmut_20, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_21': xǁSegmentedStreamReaderǁ__init____mutmut_21, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_22': xǁSegmentedStreamReaderǁ__init____mutmut_22, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_23': xǁSegmentedStreamReaderǁ__init____mutmut_23, 
        'xǁSegmentedStreamReaderǁ__init____mutmut_24': xǁSegmentedStreamReaderǁ__init____mutmut_24
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamReaderǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamReaderǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁSegmentedStreamReaderǁ__init____mutmut_orig)
    xǁSegmentedStreamReaderǁ__init____mutmut_orig.__name__ = 'xǁSegmentedStreamReaderǁ__init__'

    def open(self) -> None:
        self.writer.start()
        self.worker.start()

    def xǁSegmentedStreamReaderǁclose__mutmut_orig(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_1(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = None
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_2(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_3(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker or self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_4(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=None)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_5(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_6(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer or self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=self.timeout)

        super().close()

    def xǁSegmentedStreamReaderǁclose__mutmut_7(self) -> None:
        self.worker.close()
        self.writer.close()
        self.buffer.close()

        current = current_thread()
        if current is not self.worker and self.worker.is_alive():  # pragma: no branch
            self.worker.join(timeout=self.timeout)
        if current is not self.writer and self.writer.is_alive():  # pragma: no branch
            self.writer.join(timeout=None)

        super().close()
    
    xǁSegmentedStreamReaderǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamReaderǁclose__mutmut_1': xǁSegmentedStreamReaderǁclose__mutmut_1, 
        'xǁSegmentedStreamReaderǁclose__mutmut_2': xǁSegmentedStreamReaderǁclose__mutmut_2, 
        'xǁSegmentedStreamReaderǁclose__mutmut_3': xǁSegmentedStreamReaderǁclose__mutmut_3, 
        'xǁSegmentedStreamReaderǁclose__mutmut_4': xǁSegmentedStreamReaderǁclose__mutmut_4, 
        'xǁSegmentedStreamReaderǁclose__mutmut_5': xǁSegmentedStreamReaderǁclose__mutmut_5, 
        'xǁSegmentedStreamReaderǁclose__mutmut_6': xǁSegmentedStreamReaderǁclose__mutmut_6, 
        'xǁSegmentedStreamReaderǁclose__mutmut_7': xǁSegmentedStreamReaderǁclose__mutmut_7
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamReaderǁclose__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamReaderǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁSegmentedStreamReaderǁclose__mutmut_orig)
    xǁSegmentedStreamReaderǁclose__mutmut_orig.__name__ = 'xǁSegmentedStreamReaderǁclose'

    def xǁSegmentedStreamReaderǁread__mutmut_orig(self, size: int) -> bytes:
        return self.buffer.read(
            size,
            block=self.writer.is_alive(),
            timeout=self.timeout,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_1(self, size: int) -> bytes:
        return self.buffer.read(
            None,
            block=self.writer.is_alive(),
            timeout=self.timeout,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_2(self, size: int) -> bytes:
        return self.buffer.read(
            size,
            block=None,
            timeout=self.timeout,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_3(self, size: int) -> bytes:
        return self.buffer.read(
            size,
            block=self.writer.is_alive(),
            timeout=None,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_4(self, size: int) -> bytes:
        return self.buffer.read(
            block=self.writer.is_alive(),
            timeout=self.timeout,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_5(self, size: int) -> bytes:
        return self.buffer.read(
            size,
            timeout=self.timeout,
        )

    def xǁSegmentedStreamReaderǁread__mutmut_6(self, size: int) -> bytes:
        return self.buffer.read(
            size,
            block=self.writer.is_alive(),
            )
    
    xǁSegmentedStreamReaderǁread__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSegmentedStreamReaderǁread__mutmut_1': xǁSegmentedStreamReaderǁread__mutmut_1, 
        'xǁSegmentedStreamReaderǁread__mutmut_2': xǁSegmentedStreamReaderǁread__mutmut_2, 
        'xǁSegmentedStreamReaderǁread__mutmut_3': xǁSegmentedStreamReaderǁread__mutmut_3, 
        'xǁSegmentedStreamReaderǁread__mutmut_4': xǁSegmentedStreamReaderǁread__mutmut_4, 
        'xǁSegmentedStreamReaderǁread__mutmut_5': xǁSegmentedStreamReaderǁread__mutmut_5, 
        'xǁSegmentedStreamReaderǁread__mutmut_6': xǁSegmentedStreamReaderǁread__mutmut_6
    }
    
    def read(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSegmentedStreamReaderǁread__mutmut_orig"), object.__getattribute__(self, "xǁSegmentedStreamReaderǁread__mutmut_mutants"), args, kwargs, self)
        return result 
    
    read.__signature__ = _mutmut_signature(xǁSegmentedStreamReaderǁread__mutmut_orig)
    xǁSegmentedStreamReaderǁread__mutmut_orig.__name__ = 'xǁSegmentedStreamReaderǁread'

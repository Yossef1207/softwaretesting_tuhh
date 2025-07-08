from __future__ import annotations

import errno
import logging
from contextlib import suppress
from threading import Event, Lock, Thread

from streamlink.stream.stream import StreamIO
from streamlink_cli.console.progress import Progress
from streamlink_cli.output import HTTPOutput, Output, PlayerOutput


# Use the main Streamlink CLI module as logger
log = logging.getLogger("streamlink.cli")


ACCEPTABLE_ERRNO = errno.EPIPE, errno.EINVAL, errno.ECONNRESET
with suppress(AttributeError):
    ACCEPTABLE_ERRNO += (errno.WSAECONNABORTED,)  # type: ignore[assignment,attr-defined]
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


def _noop(_):
    return None


class _ReadError(BaseException):
    pass


class PlayerPollThread(Thread):
    """
    Poll the player process in a separate thread, to isolate it from the stream's read-loop in the main thread.
    Reading the stream can stall indefinitely when filtering content.
    """

    POLLING_INTERVAL: float = 0.5

    def xǁPlayerPollThreadǁ__init____mutmut_orig(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_1(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=None, name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_2(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=None)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_3(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_4(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, )
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_5(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=False, name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_6(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=self.__class__.__name__)
        self._stream = None
        self._output = output
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_7(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=self.__class__.__name__)
        self._stream = stream
        self._output = None
        self._stop_polling = Event()
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_8(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = None
        self._lock = Lock()

    def xǁPlayerPollThreadǁ__init____mutmut_9(self, stream: StreamIO, output: PlayerOutput):
        super().__init__(daemon=True, name=self.__class__.__name__)
        self._stream = stream
        self._output = output
        self._stop_polling = Event()
        self._lock = None
    
    xǁPlayerPollThreadǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerPollThreadǁ__init____mutmut_1': xǁPlayerPollThreadǁ__init____mutmut_1, 
        'xǁPlayerPollThreadǁ__init____mutmut_2': xǁPlayerPollThreadǁ__init____mutmut_2, 
        'xǁPlayerPollThreadǁ__init____mutmut_3': xǁPlayerPollThreadǁ__init____mutmut_3, 
        'xǁPlayerPollThreadǁ__init____mutmut_4': xǁPlayerPollThreadǁ__init____mutmut_4, 
        'xǁPlayerPollThreadǁ__init____mutmut_5': xǁPlayerPollThreadǁ__init____mutmut_5, 
        'xǁPlayerPollThreadǁ__init____mutmut_6': xǁPlayerPollThreadǁ__init____mutmut_6, 
        'xǁPlayerPollThreadǁ__init____mutmut_7': xǁPlayerPollThreadǁ__init____mutmut_7, 
        'xǁPlayerPollThreadǁ__init____mutmut_8': xǁPlayerPollThreadǁ__init____mutmut_8, 
        'xǁPlayerPollThreadǁ__init____mutmut_9': xǁPlayerPollThreadǁ__init____mutmut_9
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerPollThreadǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPlayerPollThreadǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPlayerPollThreadǁ__init____mutmut_orig)
    xǁPlayerPollThreadǁ__init____mutmut_orig.__name__ = 'xǁPlayerPollThreadǁ__init__'

    def close(self):
        self._stop_polling.set()

    def xǁPlayerPollThreadǁplayerclosed__mutmut_orig(self):
        # Ensure that "Player closed" does only get logged once, either when writing the read stream data has failed,
        # or when the player process was terminated/killed before writing.
        with self._lock:
            if self._stop_polling.is_set():
                return
            self.close()
            log.info("Player closed")

    def xǁPlayerPollThreadǁplayerclosed__mutmut_1(self):
        # Ensure that "Player closed" does only get logged once, either when writing the read stream data has failed,
        # or when the player process was terminated/killed before writing.
        with self._lock:
            if self._stop_polling.is_set():
                return
            self.close()
            log.info(None)

    def xǁPlayerPollThreadǁplayerclosed__mutmut_2(self):
        # Ensure that "Player closed" does only get logged once, either when writing the read stream data has failed,
        # or when the player process was terminated/killed before writing.
        with self._lock:
            if self._stop_polling.is_set():
                return
            self.close()
            log.info("XXPlayer closedXX")

    def xǁPlayerPollThreadǁplayerclosed__mutmut_3(self):
        # Ensure that "Player closed" does only get logged once, either when writing the read stream data has failed,
        # or when the player process was terminated/killed before writing.
        with self._lock:
            if self._stop_polling.is_set():
                return
            self.close()
            log.info("player closed")

    def xǁPlayerPollThreadǁplayerclosed__mutmut_4(self):
        # Ensure that "Player closed" does only get logged once, either when writing the read stream data has failed,
        # or when the player process was terminated/killed before writing.
        with self._lock:
            if self._stop_polling.is_set():
                return
            self.close()
            log.info("PLAYER CLOSED")
    
    xǁPlayerPollThreadǁplayerclosed__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerPollThreadǁplayerclosed__mutmut_1': xǁPlayerPollThreadǁplayerclosed__mutmut_1, 
        'xǁPlayerPollThreadǁplayerclosed__mutmut_2': xǁPlayerPollThreadǁplayerclosed__mutmut_2, 
        'xǁPlayerPollThreadǁplayerclosed__mutmut_3': xǁPlayerPollThreadǁplayerclosed__mutmut_3, 
        'xǁPlayerPollThreadǁplayerclosed__mutmut_4': xǁPlayerPollThreadǁplayerclosed__mutmut_4
    }
    
    def playerclosed(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerPollThreadǁplayerclosed__mutmut_orig"), object.__getattribute__(self, "xǁPlayerPollThreadǁplayerclosed__mutmut_mutants"), args, kwargs, self)
        return result 
    
    playerclosed.__signature__ = _mutmut_signature(xǁPlayerPollThreadǁplayerclosed__mutmut_orig)
    xǁPlayerPollThreadǁplayerclosed__mutmut_orig.__name__ = 'xǁPlayerPollThreadǁplayerclosed'

    def xǁPlayerPollThreadǁpoll__mutmut_orig(self) -> bool:
        return self._output.player.poll() is None

    def xǁPlayerPollThreadǁpoll__mutmut_1(self) -> bool:
        return self._output.player.poll() is not None
    
    xǁPlayerPollThreadǁpoll__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerPollThreadǁpoll__mutmut_1': xǁPlayerPollThreadǁpoll__mutmut_1
    }
    
    def poll(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerPollThreadǁpoll__mutmut_orig"), object.__getattribute__(self, "xǁPlayerPollThreadǁpoll__mutmut_mutants"), args, kwargs, self)
        return result 
    
    poll.__signature__ = _mutmut_signature(xǁPlayerPollThreadǁpoll__mutmut_orig)
    xǁPlayerPollThreadǁpoll__mutmut_orig.__name__ = 'xǁPlayerPollThreadǁpoll'

    def xǁPlayerPollThreadǁrun__mutmut_orig(self) -> None:
        while not self._stop_polling.wait(self.POLLING_INTERVAL):
            if self.poll():
                continue
            self.playerclosed()
            # close stream as soon as the player was closed
            self._stream.close()
            break

    def xǁPlayerPollThreadǁrun__mutmut_1(self) -> None:
        while self._stop_polling.wait(self.POLLING_INTERVAL):
            if self.poll():
                continue
            self.playerclosed()
            # close stream as soon as the player was closed
            self._stream.close()
            break

    def xǁPlayerPollThreadǁrun__mutmut_2(self) -> None:
        while not self._stop_polling.wait(None):
            if self.poll():
                continue
            self.playerclosed()
            # close stream as soon as the player was closed
            self._stream.close()
            break

    def xǁPlayerPollThreadǁrun__mutmut_3(self) -> None:
        while not self._stop_polling.wait(self.POLLING_INTERVAL):
            if self.poll():
                break
            self.playerclosed()
            # close stream as soon as the player was closed
            self._stream.close()
            break

    def xǁPlayerPollThreadǁrun__mutmut_4(self) -> None:
        while not self._stop_polling.wait(self.POLLING_INTERVAL):
            if self.poll():
                continue
            self.playerclosed()
            # close stream as soon as the player was closed
            self._stream.close()
            return
    
    xǁPlayerPollThreadǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerPollThreadǁrun__mutmut_1': xǁPlayerPollThreadǁrun__mutmut_1, 
        'xǁPlayerPollThreadǁrun__mutmut_2': xǁPlayerPollThreadǁrun__mutmut_2, 
        'xǁPlayerPollThreadǁrun__mutmut_3': xǁPlayerPollThreadǁrun__mutmut_3, 
        'xǁPlayerPollThreadǁrun__mutmut_4': xǁPlayerPollThreadǁrun__mutmut_4
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerPollThreadǁrun__mutmut_orig"), object.__getattribute__(self, "xǁPlayerPollThreadǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁPlayerPollThreadǁrun__mutmut_orig)
    xǁPlayerPollThreadǁrun__mutmut_orig.__name__ = 'xǁPlayerPollThreadǁrun'


class StreamRunner:
    """Read data from a stream and write it to the output."""

    playerpoller: PlayerPollThread | None = None

    def xǁStreamRunnerǁ__init____mutmut_orig(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, output)

    def xǁStreamRunnerǁ__init____mutmut_1(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = None
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, output)

    def xǁStreamRunnerǁ__init____mutmut_2(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = None
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, output)

    def xǁStreamRunnerǁ__init____mutmut_3(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = None

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, output)

    def xǁStreamRunnerǁ__init____mutmut_4(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = None

    def xǁStreamRunnerǁ__init____mutmut_5(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(None, output)

    def xǁStreamRunnerǁ__init____mutmut_6(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, None)

    def xǁStreamRunnerǁ__init____mutmut_7(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(output)

    def xǁStreamRunnerǁ__init____mutmut_8(
        self,
        stream: StreamIO,
        output: Output,
        progress: Progress | None = None,
    ):
        self.stream = stream
        self.output = output
        self.progress = progress

        if isinstance(output, PlayerOutput):
            self.playerpoller = PlayerPollThread(stream, )
    
    xǁStreamRunnerǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamRunnerǁ__init____mutmut_1': xǁStreamRunnerǁ__init____mutmut_1, 
        'xǁStreamRunnerǁ__init____mutmut_2': xǁStreamRunnerǁ__init____mutmut_2, 
        'xǁStreamRunnerǁ__init____mutmut_3': xǁStreamRunnerǁ__init____mutmut_3, 
        'xǁStreamRunnerǁ__init____mutmut_4': xǁStreamRunnerǁ__init____mutmut_4, 
        'xǁStreamRunnerǁ__init____mutmut_5': xǁStreamRunnerǁ__init____mutmut_5, 
        'xǁStreamRunnerǁ__init____mutmut_6': xǁStreamRunnerǁ__init____mutmut_6, 
        'xǁStreamRunnerǁ__init____mutmut_7': xǁStreamRunnerǁ__init____mutmut_7, 
        'xǁStreamRunnerǁ__init____mutmut_8': xǁStreamRunnerǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamRunnerǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁStreamRunnerǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁStreamRunnerǁ__init____mutmut_orig)
    xǁStreamRunnerǁ__init____mutmut_orig.__name__ = 'xǁStreamRunnerǁ__init__'

    def xǁStreamRunnerǁrun__mutmut_orig(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_1(
        self,
        prebuffer: bytes,
        chunk_size: int = 8193,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_2(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = None
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_3(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = None
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_4(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = None

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_5(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = None

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_6(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(None)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_7(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(None)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_8(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while False:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_9(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = None
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_10(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(None)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_11(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data != b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_12(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"XXXX":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_13(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_14(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_15(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_16(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        return
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_17(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(None)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_18(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(None)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_19(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(None) from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_20(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller or err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_21(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno not in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_22(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) or err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_23(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno not in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_24(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info(None)
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_25(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("XXHTTP connection closedXX")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_26(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("http connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_27(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP CONNECTION CLOSED")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_28(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("Http connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_29(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(None) from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("Stream ended")

    def xǁStreamRunnerǁrun__mutmut_30(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info(None)

    def xǁStreamRunnerǁrun__mutmut_31(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("XXStream endedXX")

    def xǁStreamRunnerǁrun__mutmut_32(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("stream ended")

    def xǁStreamRunnerǁrun__mutmut_33(
        self,
        prebuffer: bytes,
        chunk_size: int = 8192,
    ) -> None:
        read = self.stream.read
        write = self.output.write
        progress = _noop

        if self.playerpoller:
            self.playerpoller.start()
        if self.progress:
            self.progress.start()
            progress = self.progress.write

        # TODO: Fix error messages (s/when/while/) and only log "Stream ended" when it ended on its own (data == b"").
        #       These are considered breaking changes of the CLI output, which is parsed by 3rd party tools.
        try:
            write(prebuffer)
            progress(prebuffer)
            del prebuffer

            # Don't check for stream.closed, so the buffer's contents can be fully read after the stream ended or was closed
            while True:
                try:
                    data = read(chunk_size)
                    if data == b"":
                        break
                except OSError as err:
                    raise _ReadError() from err

                write(data)
                progress(data)

        except _ReadError as err:
            raise OSError(f"Error when reading from stream: {err.__context__}, exiting") from err.__context__

        except OSError as err:
            if self.playerpoller and err.errno in ACCEPTABLE_ERRNO:
                self.playerpoller.playerclosed()
            elif isinstance(self.output, HTTPOutput) and err.errno in ACCEPTABLE_ERRNO:
                log.info("HTTP connection closed")
            else:
                raise OSError(f"Error when writing to output: {err}, exiting") from err

        finally:
            if self.playerpoller:
                self.playerpoller.close()
                self.playerpoller.join()
            if self.progress:
                self.progress.close()
                self.progress.join()

            self.stream.close()
            log.info("STREAM ENDED")
    
    xǁStreamRunnerǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁStreamRunnerǁrun__mutmut_1': xǁStreamRunnerǁrun__mutmut_1, 
        'xǁStreamRunnerǁrun__mutmut_2': xǁStreamRunnerǁrun__mutmut_2, 
        'xǁStreamRunnerǁrun__mutmut_3': xǁStreamRunnerǁrun__mutmut_3, 
        'xǁStreamRunnerǁrun__mutmut_4': xǁStreamRunnerǁrun__mutmut_4, 
        'xǁStreamRunnerǁrun__mutmut_5': xǁStreamRunnerǁrun__mutmut_5, 
        'xǁStreamRunnerǁrun__mutmut_6': xǁStreamRunnerǁrun__mutmut_6, 
        'xǁStreamRunnerǁrun__mutmut_7': xǁStreamRunnerǁrun__mutmut_7, 
        'xǁStreamRunnerǁrun__mutmut_8': xǁStreamRunnerǁrun__mutmut_8, 
        'xǁStreamRunnerǁrun__mutmut_9': xǁStreamRunnerǁrun__mutmut_9, 
        'xǁStreamRunnerǁrun__mutmut_10': xǁStreamRunnerǁrun__mutmut_10, 
        'xǁStreamRunnerǁrun__mutmut_11': xǁStreamRunnerǁrun__mutmut_11, 
        'xǁStreamRunnerǁrun__mutmut_12': xǁStreamRunnerǁrun__mutmut_12, 
        'xǁStreamRunnerǁrun__mutmut_13': xǁStreamRunnerǁrun__mutmut_13, 
        'xǁStreamRunnerǁrun__mutmut_14': xǁStreamRunnerǁrun__mutmut_14, 
        'xǁStreamRunnerǁrun__mutmut_15': xǁStreamRunnerǁrun__mutmut_15, 
        'xǁStreamRunnerǁrun__mutmut_16': xǁStreamRunnerǁrun__mutmut_16, 
        'xǁStreamRunnerǁrun__mutmut_17': xǁStreamRunnerǁrun__mutmut_17, 
        'xǁStreamRunnerǁrun__mutmut_18': xǁStreamRunnerǁrun__mutmut_18, 
        'xǁStreamRunnerǁrun__mutmut_19': xǁStreamRunnerǁrun__mutmut_19, 
        'xǁStreamRunnerǁrun__mutmut_20': xǁStreamRunnerǁrun__mutmut_20, 
        'xǁStreamRunnerǁrun__mutmut_21': xǁStreamRunnerǁrun__mutmut_21, 
        'xǁStreamRunnerǁrun__mutmut_22': xǁStreamRunnerǁrun__mutmut_22, 
        'xǁStreamRunnerǁrun__mutmut_23': xǁStreamRunnerǁrun__mutmut_23, 
        'xǁStreamRunnerǁrun__mutmut_24': xǁStreamRunnerǁrun__mutmut_24, 
        'xǁStreamRunnerǁrun__mutmut_25': xǁStreamRunnerǁrun__mutmut_25, 
        'xǁStreamRunnerǁrun__mutmut_26': xǁStreamRunnerǁrun__mutmut_26, 
        'xǁStreamRunnerǁrun__mutmut_27': xǁStreamRunnerǁrun__mutmut_27, 
        'xǁStreamRunnerǁrun__mutmut_28': xǁStreamRunnerǁrun__mutmut_28, 
        'xǁStreamRunnerǁrun__mutmut_29': xǁStreamRunnerǁrun__mutmut_29, 
        'xǁStreamRunnerǁrun__mutmut_30': xǁStreamRunnerǁrun__mutmut_30, 
        'xǁStreamRunnerǁrun__mutmut_31': xǁStreamRunnerǁrun__mutmut_31, 
        'xǁStreamRunnerǁrun__mutmut_32': xǁStreamRunnerǁrun__mutmut_32, 
        'xǁStreamRunnerǁrun__mutmut_33': xǁStreamRunnerǁrun__mutmut_33
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁStreamRunnerǁrun__mutmut_orig"), object.__getattribute__(self, "xǁStreamRunnerǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁStreamRunnerǁrun__mutmut_orig)
    xǁStreamRunnerǁrun__mutmut_orig.__name__ = 'xǁStreamRunnerǁrun'

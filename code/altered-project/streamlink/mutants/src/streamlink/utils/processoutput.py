from __future__ import annotations

import math
from collections.abc import Callable
from contextlib import suppress
from functools import partial
from subprocess import PIPE
from typing import BinaryIO

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


class ProcessOutput:
    _send_channel: trio.MemorySendChannel[bool]
    _receive_channel: trio.MemoryReceiveChannel[bool]

    def xǁProcessOutputǁ__init____mutmut_orig(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_1(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 3.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_2(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = None
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_3(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = None
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_4(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = None
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_5(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = None
        self._send_channel, self._receive_channel = trio.open_memory_channel(1)

    def xǁProcessOutputǁ__init____mutmut_6(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = None

    def xǁProcessOutputǁ__init____mutmut_7(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(None)

    def xǁProcessOutputǁ__init____mutmut_8(
        self,
        command: list[str],
        timeout: float = math.inf,
        wait_terminate: float = 2.0,
        stdin: int | bytes | BinaryIO | None = PIPE,
    ):
        self.command = command
        self.timeout = timeout
        self.wait_terminate = wait_terminate
        self.stdin = stdin
        self._send_channel, self._receive_channel = trio.open_memory_channel(2)
    
    xǁProcessOutputǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁ__init____mutmut_1': xǁProcessOutputǁ__init____mutmut_1, 
        'xǁProcessOutputǁ__init____mutmut_2': xǁProcessOutputǁ__init____mutmut_2, 
        'xǁProcessOutputǁ__init____mutmut_3': xǁProcessOutputǁ__init____mutmut_3, 
        'xǁProcessOutputǁ__init____mutmut_4': xǁProcessOutputǁ__init____mutmut_4, 
        'xǁProcessOutputǁ__init____mutmut_5': xǁProcessOutputǁ__init____mutmut_5, 
        'xǁProcessOutputǁ__init____mutmut_6': xǁProcessOutputǁ__init____mutmut_6, 
        'xǁProcessOutputǁ__init____mutmut_7': xǁProcessOutputǁ__init____mutmut_7, 
        'xǁProcessOutputǁ__init____mutmut_8': xǁProcessOutputǁ__init____mutmut_8
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁProcessOutputǁ__init____mutmut_orig)
    xǁProcessOutputǁ__init____mutmut_orig.__name__ = 'xǁProcessOutputǁ__init__'

    def xǁProcessOutputǁrun__mutmut_orig(self) -> bool:  # pragma: no cover
        return trio.run(self.arun)

    def xǁProcessOutputǁrun__mutmut_1(self) -> bool:  # pragma: no cover
        return trio.run(None)
    
    xǁProcessOutputǁrun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁrun__mutmut_1': xǁProcessOutputǁrun__mutmut_1
    }
    
    def run(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁrun__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁrun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    run.__signature__ = _mutmut_signature(xǁProcessOutputǁrun__mutmut_orig)
    xǁProcessOutputǁrun__mutmut_orig.__name__ = 'xǁProcessOutputǁrun'

    async def xǁProcessOutputǁarun__mutmut_orig(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_1(self) -> bool:
        with trio.move_on_after(None):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_2(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = None
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_3(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    None,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_4(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    None,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_5(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=None,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_6(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=None,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_7(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=None,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_8(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=None,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_9(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=None,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_10(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=None,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_11(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=None,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_12(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_13(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_14(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_15(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_16(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_17(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_18(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_19(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_20(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_21(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=True,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_22(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=True,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_23(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=True,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_24(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = None

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_25(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(None)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_26(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(None, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_27(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, None)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_28(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_29(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, )
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_30(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(None, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_31(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, None, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_32(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, None)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_33(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_34(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_35(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, )
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_36(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(None, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_37(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, None, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_38(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, None)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_39(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_40(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_41(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, )

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_42(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = None
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return False

    async def xǁProcessOutputǁarun__mutmut_43(self) -> bool:
        with trio.move_on_after(self.timeout):
            async with trio.open_nursery() as nursery:
                run_process = partial(
                    trio.run_process,
                    self.command,
                    check=False,
                    capture_stdout=False,
                    capture_stderr=False,
                    stdin=self.stdin,
                    stdout=PIPE,
                    stderr=PIPE,
                    deliver_cancel=self._deliver_cancel,
                )
                process: trio.Process = await nursery.start(run_process)

                nursery.start_soon(self._onexit, process)
                nursery.start_soon(self._onoutput, self.onstdout, process.stdout)
                nursery.start_soon(self._onoutput, self.onstderr, process.stderr)

                res = await self._receive_channel.receive()
                nursery.cancel_scope.cancel()
                return res

        # noinspection PyUnreachableCode
        return True
    
    xǁProcessOutputǁarun__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁarun__mutmut_1': xǁProcessOutputǁarun__mutmut_1, 
        'xǁProcessOutputǁarun__mutmut_2': xǁProcessOutputǁarun__mutmut_2, 
        'xǁProcessOutputǁarun__mutmut_3': xǁProcessOutputǁarun__mutmut_3, 
        'xǁProcessOutputǁarun__mutmut_4': xǁProcessOutputǁarun__mutmut_4, 
        'xǁProcessOutputǁarun__mutmut_5': xǁProcessOutputǁarun__mutmut_5, 
        'xǁProcessOutputǁarun__mutmut_6': xǁProcessOutputǁarun__mutmut_6, 
        'xǁProcessOutputǁarun__mutmut_7': xǁProcessOutputǁarun__mutmut_7, 
        'xǁProcessOutputǁarun__mutmut_8': xǁProcessOutputǁarun__mutmut_8, 
        'xǁProcessOutputǁarun__mutmut_9': xǁProcessOutputǁarun__mutmut_9, 
        'xǁProcessOutputǁarun__mutmut_10': xǁProcessOutputǁarun__mutmut_10, 
        'xǁProcessOutputǁarun__mutmut_11': xǁProcessOutputǁarun__mutmut_11, 
        'xǁProcessOutputǁarun__mutmut_12': xǁProcessOutputǁarun__mutmut_12, 
        'xǁProcessOutputǁarun__mutmut_13': xǁProcessOutputǁarun__mutmut_13, 
        'xǁProcessOutputǁarun__mutmut_14': xǁProcessOutputǁarun__mutmut_14, 
        'xǁProcessOutputǁarun__mutmut_15': xǁProcessOutputǁarun__mutmut_15, 
        'xǁProcessOutputǁarun__mutmut_16': xǁProcessOutputǁarun__mutmut_16, 
        'xǁProcessOutputǁarun__mutmut_17': xǁProcessOutputǁarun__mutmut_17, 
        'xǁProcessOutputǁarun__mutmut_18': xǁProcessOutputǁarun__mutmut_18, 
        'xǁProcessOutputǁarun__mutmut_19': xǁProcessOutputǁarun__mutmut_19, 
        'xǁProcessOutputǁarun__mutmut_20': xǁProcessOutputǁarun__mutmut_20, 
        'xǁProcessOutputǁarun__mutmut_21': xǁProcessOutputǁarun__mutmut_21, 
        'xǁProcessOutputǁarun__mutmut_22': xǁProcessOutputǁarun__mutmut_22, 
        'xǁProcessOutputǁarun__mutmut_23': xǁProcessOutputǁarun__mutmut_23, 
        'xǁProcessOutputǁarun__mutmut_24': xǁProcessOutputǁarun__mutmut_24, 
        'xǁProcessOutputǁarun__mutmut_25': xǁProcessOutputǁarun__mutmut_25, 
        'xǁProcessOutputǁarun__mutmut_26': xǁProcessOutputǁarun__mutmut_26, 
        'xǁProcessOutputǁarun__mutmut_27': xǁProcessOutputǁarun__mutmut_27, 
        'xǁProcessOutputǁarun__mutmut_28': xǁProcessOutputǁarun__mutmut_28, 
        'xǁProcessOutputǁarun__mutmut_29': xǁProcessOutputǁarun__mutmut_29, 
        'xǁProcessOutputǁarun__mutmut_30': xǁProcessOutputǁarun__mutmut_30, 
        'xǁProcessOutputǁarun__mutmut_31': xǁProcessOutputǁarun__mutmut_31, 
        'xǁProcessOutputǁarun__mutmut_32': xǁProcessOutputǁarun__mutmut_32, 
        'xǁProcessOutputǁarun__mutmut_33': xǁProcessOutputǁarun__mutmut_33, 
        'xǁProcessOutputǁarun__mutmut_34': xǁProcessOutputǁarun__mutmut_34, 
        'xǁProcessOutputǁarun__mutmut_35': xǁProcessOutputǁarun__mutmut_35, 
        'xǁProcessOutputǁarun__mutmut_36': xǁProcessOutputǁarun__mutmut_36, 
        'xǁProcessOutputǁarun__mutmut_37': xǁProcessOutputǁarun__mutmut_37, 
        'xǁProcessOutputǁarun__mutmut_38': xǁProcessOutputǁarun__mutmut_38, 
        'xǁProcessOutputǁarun__mutmut_39': xǁProcessOutputǁarun__mutmut_39, 
        'xǁProcessOutputǁarun__mutmut_40': xǁProcessOutputǁarun__mutmut_40, 
        'xǁProcessOutputǁarun__mutmut_41': xǁProcessOutputǁarun__mutmut_41, 
        'xǁProcessOutputǁarun__mutmut_42': xǁProcessOutputǁarun__mutmut_42, 
        'xǁProcessOutputǁarun__mutmut_43': xǁProcessOutputǁarun__mutmut_43
    }
    
    def arun(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁarun__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁarun__mutmut_mutants"), args, kwargs, self)
        return result 
    
    arun.__signature__ = _mutmut_signature(xǁProcessOutputǁarun__mutmut_orig)
    xǁProcessOutputǁarun__mutmut_orig.__name__ = 'xǁProcessOutputǁarun'

    async def xǁProcessOutputǁ_deliver_cancel__mutmut_orig(self, proc: trio.Process):
        with suppress(OSError):
            proc.terminate()
            await trio.sleep(self.wait_terminate)
            proc.kill()

    async def xǁProcessOutputǁ_deliver_cancel__mutmut_1(self, proc: trio.Process):
        with suppress(None):
            proc.terminate()
            await trio.sleep(self.wait_terminate)
            proc.kill()

    async def xǁProcessOutputǁ_deliver_cancel__mutmut_2(self, proc: trio.Process):
        with suppress(OSError):
            proc.terminate()
            await trio.sleep(None)
            proc.kill()
    
    xǁProcessOutputǁ_deliver_cancel__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁ_deliver_cancel__mutmut_1': xǁProcessOutputǁ_deliver_cancel__mutmut_1, 
        'xǁProcessOutputǁ_deliver_cancel__mutmut_2': xǁProcessOutputǁ_deliver_cancel__mutmut_2
    }
    
    def _deliver_cancel(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁ_deliver_cancel__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁ_deliver_cancel__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _deliver_cancel.__signature__ = _mutmut_signature(xǁProcessOutputǁ_deliver_cancel__mutmut_orig)
    xǁProcessOutputǁ_deliver_cancel__mutmut_orig.__name__ = 'xǁProcessOutputǁ_deliver_cancel'

    async def xǁProcessOutputǁ_onexit__mutmut_orig(self, proc: trio.Process):
        code = await proc.wait()
        result = self.onexit(code)
        await self._send_channel.send(result)

    async def xǁProcessOutputǁ_onexit__mutmut_1(self, proc: trio.Process):
        code = None
        result = self.onexit(code)
        await self._send_channel.send(result)

    async def xǁProcessOutputǁ_onexit__mutmut_2(self, proc: trio.Process):
        code = await proc.wait()
        result = None
        await self._send_channel.send(result)

    async def xǁProcessOutputǁ_onexit__mutmut_3(self, proc: trio.Process):
        code = await proc.wait()
        result = self.onexit(None)
        await self._send_channel.send(result)

    async def xǁProcessOutputǁ_onexit__mutmut_4(self, proc: trio.Process):
        code = await proc.wait()
        result = self.onexit(code)
        await self._send_channel.send(None)
    
    xǁProcessOutputǁ_onexit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁ_onexit__mutmut_1': xǁProcessOutputǁ_onexit__mutmut_1, 
        'xǁProcessOutputǁ_onexit__mutmut_2': xǁProcessOutputǁ_onexit__mutmut_2, 
        'xǁProcessOutputǁ_onexit__mutmut_3': xǁProcessOutputǁ_onexit__mutmut_3, 
        'xǁProcessOutputǁ_onexit__mutmut_4': xǁProcessOutputǁ_onexit__mutmut_4
    }
    
    def _onexit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁ_onexit__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁ_onexit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _onexit.__signature__ = _mutmut_signature(xǁProcessOutputǁ_onexit__mutmut_orig)
    xǁProcessOutputǁ_onexit__mutmut_orig.__name__ = 'xǁProcessOutputǁ_onexit'

    async def xǁProcessOutputǁ_onoutput__mutmut_orig(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_1(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = None
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_2(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 1
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_3(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = None
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_4(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode(None).strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_5(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("XXutf-8XX").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_6(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("UTF-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_7(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("Utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_8(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = None
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_9(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(None, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_10(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, None)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_11(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_12(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, )
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_13(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is None:
                await self._send_channel.send(bool(result))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_14(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(None)
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_15(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(None))
                break
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_16(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                return
            idx += 1

    async def xǁProcessOutputǁ_onoutput__mutmut_17(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx = 1

    async def xǁProcessOutputǁ_onoutput__mutmut_18(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx -= 1

    async def xǁProcessOutputǁ_onoutput__mutmut_19(self, callback: Callable[[int, str], bool | None], stream: trio.abc.ReceiveChannel[bytes]):
        idx = 0
        async for line in stream:
            try:
                content = line.decode("utf-8").strip()
                result = callback(idx, content)
            except Exception:
                raise
            if result is not None:
                await self._send_channel.send(bool(result))
                break
            idx += 2
    
    xǁProcessOutputǁ_onoutput__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁ_onoutput__mutmut_1': xǁProcessOutputǁ_onoutput__mutmut_1, 
        'xǁProcessOutputǁ_onoutput__mutmut_2': xǁProcessOutputǁ_onoutput__mutmut_2, 
        'xǁProcessOutputǁ_onoutput__mutmut_3': xǁProcessOutputǁ_onoutput__mutmut_3, 
        'xǁProcessOutputǁ_onoutput__mutmut_4': xǁProcessOutputǁ_onoutput__mutmut_4, 
        'xǁProcessOutputǁ_onoutput__mutmut_5': xǁProcessOutputǁ_onoutput__mutmut_5, 
        'xǁProcessOutputǁ_onoutput__mutmut_6': xǁProcessOutputǁ_onoutput__mutmut_6, 
        'xǁProcessOutputǁ_onoutput__mutmut_7': xǁProcessOutputǁ_onoutput__mutmut_7, 
        'xǁProcessOutputǁ_onoutput__mutmut_8': xǁProcessOutputǁ_onoutput__mutmut_8, 
        'xǁProcessOutputǁ_onoutput__mutmut_9': xǁProcessOutputǁ_onoutput__mutmut_9, 
        'xǁProcessOutputǁ_onoutput__mutmut_10': xǁProcessOutputǁ_onoutput__mutmut_10, 
        'xǁProcessOutputǁ_onoutput__mutmut_11': xǁProcessOutputǁ_onoutput__mutmut_11, 
        'xǁProcessOutputǁ_onoutput__mutmut_12': xǁProcessOutputǁ_onoutput__mutmut_12, 
        'xǁProcessOutputǁ_onoutput__mutmut_13': xǁProcessOutputǁ_onoutput__mutmut_13, 
        'xǁProcessOutputǁ_onoutput__mutmut_14': xǁProcessOutputǁ_onoutput__mutmut_14, 
        'xǁProcessOutputǁ_onoutput__mutmut_15': xǁProcessOutputǁ_onoutput__mutmut_15, 
        'xǁProcessOutputǁ_onoutput__mutmut_16': xǁProcessOutputǁ_onoutput__mutmut_16, 
        'xǁProcessOutputǁ_onoutput__mutmut_17': xǁProcessOutputǁ_onoutput__mutmut_17, 
        'xǁProcessOutputǁ_onoutput__mutmut_18': xǁProcessOutputǁ_onoutput__mutmut_18, 
        'xǁProcessOutputǁ_onoutput__mutmut_19': xǁProcessOutputǁ_onoutput__mutmut_19
    }
    
    def _onoutput(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁ_onoutput__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁ_onoutput__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _onoutput.__signature__ = _mutmut_signature(xǁProcessOutputǁ_onoutput__mutmut_orig)
    xǁProcessOutputǁ_onoutput__mutmut_orig.__name__ = 'xǁProcessOutputǁ_onoutput'

    def xǁProcessOutputǁonexit__mutmut_orig(self, code: int) -> bool:
        return code == 0

    def xǁProcessOutputǁonexit__mutmut_1(self, code: int) -> bool:
        return code != 0

    def xǁProcessOutputǁonexit__mutmut_2(self, code: int) -> bool:
        return code == 1
    
    xǁProcessOutputǁonexit__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁProcessOutputǁonexit__mutmut_1': xǁProcessOutputǁonexit__mutmut_1, 
        'xǁProcessOutputǁonexit__mutmut_2': xǁProcessOutputǁonexit__mutmut_2
    }
    
    def onexit(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁProcessOutputǁonexit__mutmut_orig"), object.__getattribute__(self, "xǁProcessOutputǁonexit__mutmut_mutants"), args, kwargs, self)
        return result 
    
    onexit.__signature__ = _mutmut_signature(xǁProcessOutputǁonexit__mutmut_orig)
    xǁProcessOutputǁonexit__mutmut_orig.__name__ = 'xǁProcessOutputǁonexit'

    def onstdout(self, idx: int, line: str) -> bool | None:
        pass

    def onstderr(self, idx: int, line: str) -> bool | None:
        pass

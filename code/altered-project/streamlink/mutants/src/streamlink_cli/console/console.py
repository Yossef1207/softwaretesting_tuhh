from __future__ import annotations

import sys
from contextlib import contextmanager, suppress
from getpass import getpass
from json import dumps
from typing import Any, TextIO

from streamlink_cli.console.stream import ConsoleOutputStream, ConsoleStatusMessage
from streamlink_cli.utils import JSONEncoder
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


class ConsoleOutput:
    def xǁConsoleOutputǁ__init____mutmut_orig(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is not None and console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_1(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = True,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is not None and console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_2(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = None
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is not None and console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_3(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = None
        self._supports_status_messages: bool = console_output is not None and console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_4(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = None
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_5(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is None and console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_6(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is not None or console_output.supports_status_messages()
        self._file_output: TextIO | None = file_output
    def xǁConsoleOutputǁ__init____mutmut_7(
        self,
        *,
        console_output: ConsoleOutputStream | None = None,
        file_output: TextIO | None = None,
        json: bool = False,
    ):
        self.json: bool = json
        self._console_output: ConsoleOutputStream | None = console_output
        self._supports_status_messages: bool = console_output is not None and console_output.supports_status_messages()
        self._file_output: TextIO | None = None
    
    xǁConsoleOutputǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁ__init____mutmut_1': xǁConsoleOutputǁ__init____mutmut_1, 
        'xǁConsoleOutputǁ__init____mutmut_2': xǁConsoleOutputǁ__init____mutmut_2, 
        'xǁConsoleOutputǁ__init____mutmut_3': xǁConsoleOutputǁ__init____mutmut_3, 
        'xǁConsoleOutputǁ__init____mutmut_4': xǁConsoleOutputǁ__init____mutmut_4, 
        'xǁConsoleOutputǁ__init____mutmut_5': xǁConsoleOutputǁ__init____mutmut_5, 
        'xǁConsoleOutputǁ__init____mutmut_6': xǁConsoleOutputǁ__init____mutmut_6, 
        'xǁConsoleOutputǁ__init____mutmut_7': xǁConsoleOutputǁ__init____mutmut_7
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁConsoleOutputǁ__init____mutmut_orig)
    xǁConsoleOutputǁ__init____mutmut_orig.__name__ = 'xǁConsoleOutputǁ__init__'

    @property
    def console_output(self) -> ConsoleOutputStream | None:
        return self._console_output

    @console_output.setter
    def console_output(self, console_output: ConsoleOutputStream | None) -> None:
        self._console_output = console_output
        self._supports_status_messages = console_output is not None and console_output.supports_status_messages()

    @property
    def file_output(self) -> TextIO | None:
        return self._file_output

    @file_output.setter
    def file_output(self, file_output: TextIO | None) -> None:
        if file_output is None or file_output.isatty():
            self._file_output = None
        else:
            self._file_output = file_output

    def supports_status_messages(self) -> bool:
        return self._supports_status_messages

    def xǁConsoleOutputǁclose__mutmut_orig(self):
        if self._console_output:  # pragma: no branch
            with suppress(OSError):
                self._console_output.close()
            self._console_output.restore()
        if self._file_output:  # pragma: no branch
            with suppress(OSError):
                self._file_output.close()

    def xǁConsoleOutputǁclose__mutmut_1(self):
        if self._console_output:  # pragma: no branch
            with suppress(None):
                self._console_output.close()
            self._console_output.restore()
        if self._file_output:  # pragma: no branch
            with suppress(OSError):
                self._file_output.close()

    def xǁConsoleOutputǁclose__mutmut_2(self):
        if self._console_output:  # pragma: no branch
            with suppress(OSError):
                self._console_output.close()
            self._console_output.restore()
        if self._file_output:  # pragma: no branch
            with suppress(None):
                self._file_output.close()
    
    xǁConsoleOutputǁclose__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁclose__mutmut_1': xǁConsoleOutputǁclose__mutmut_1, 
        'xǁConsoleOutputǁclose__mutmut_2': xǁConsoleOutputǁclose__mutmut_2
    }
    
    def close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁclose__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁclose__mutmut_mutants"), args, kwargs, self)
        return result 
    
    close.__signature__ = _mutmut_signature(xǁConsoleOutputǁclose__mutmut_orig)
    xǁConsoleOutputǁclose__mutmut_orig.__name__ = 'xǁConsoleOutputǁclose'

    @staticmethod
    def _write(stream: TextIO, msg: str):
        with suppress(OSError):
            stream.write(msg)
            stream.flush()

    def xǁConsoleOutputǁ_write_console__mutmut_orig(self, msg: str):
        if self._console_output is None:
            return
        self._write(self._console_output, msg)

    def xǁConsoleOutputǁ_write_console__mutmut_1(self, msg: str):
        if self._console_output is not None:
            return
        self._write(self._console_output, msg)

    def xǁConsoleOutputǁ_write_console__mutmut_2(self, msg: str):
        if self._console_output is None:
            return
        self._write(None, msg)

    def xǁConsoleOutputǁ_write_console__mutmut_3(self, msg: str):
        if self._console_output is None:
            return
        self._write(self._console_output, None)

    def xǁConsoleOutputǁ_write_console__mutmut_4(self, msg: str):
        if self._console_output is None:
            return
        self._write(msg)

    def xǁConsoleOutputǁ_write_console__mutmut_5(self, msg: str):
        if self._console_output is None:
            return
        self._write(self._console_output, )
    
    xǁConsoleOutputǁ_write_console__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁ_write_console__mutmut_1': xǁConsoleOutputǁ_write_console__mutmut_1, 
        'xǁConsoleOutputǁ_write_console__mutmut_2': xǁConsoleOutputǁ_write_console__mutmut_2, 
        'xǁConsoleOutputǁ_write_console__mutmut_3': xǁConsoleOutputǁ_write_console__mutmut_3, 
        'xǁConsoleOutputǁ_write_console__mutmut_4': xǁConsoleOutputǁ_write_console__mutmut_4, 
        'xǁConsoleOutputǁ_write_console__mutmut_5': xǁConsoleOutputǁ_write_console__mutmut_5
    }
    
    def _write_console(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁ_write_console__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁ_write_console__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _write_console.__signature__ = _mutmut_signature(xǁConsoleOutputǁ_write_console__mutmut_orig)
    xǁConsoleOutputǁ_write_console__mutmut_orig.__name__ = 'xǁConsoleOutputǁ_write_console'

    def xǁConsoleOutputǁ_write_file__mutmut_orig(self, msg: str):
        if self._file_output is None:
            return
        self._write(self._file_output, msg)

    def xǁConsoleOutputǁ_write_file__mutmut_1(self, msg: str):
        if self._file_output is not None:
            return
        self._write(self._file_output, msg)

    def xǁConsoleOutputǁ_write_file__mutmut_2(self, msg: str):
        if self._file_output is None:
            return
        self._write(None, msg)

    def xǁConsoleOutputǁ_write_file__mutmut_3(self, msg: str):
        if self._file_output is None:
            return
        self._write(self._file_output, None)

    def xǁConsoleOutputǁ_write_file__mutmut_4(self, msg: str):
        if self._file_output is None:
            return
        self._write(msg)

    def xǁConsoleOutputǁ_write_file__mutmut_5(self, msg: str):
        if self._file_output is None:
            return
        self._write(self._file_output, )
    
    xǁConsoleOutputǁ_write_file__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁ_write_file__mutmut_1': xǁConsoleOutputǁ_write_file__mutmut_1, 
        'xǁConsoleOutputǁ_write_file__mutmut_2': xǁConsoleOutputǁ_write_file__mutmut_2, 
        'xǁConsoleOutputǁ_write_file__mutmut_3': xǁConsoleOutputǁ_write_file__mutmut_3, 
        'xǁConsoleOutputǁ_write_file__mutmut_4': xǁConsoleOutputǁ_write_file__mutmut_4, 
        'xǁConsoleOutputǁ_write_file__mutmut_5': xǁConsoleOutputǁ_write_file__mutmut_5
    }
    
    def _write_file(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁ_write_file__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁ_write_file__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _write_file.__signature__ = _mutmut_signature(xǁConsoleOutputǁ_write_file__mutmut_orig)
    xǁConsoleOutputǁ_write_file__mutmut_orig.__name__ = 'xǁConsoleOutputǁ_write_file'

    @contextmanager
    def _prompt(self):
        if not sys.stdin or not sys.stdin.isatty():
            raise OSError("No input TTY available")
        if not self._console_output or not self._console_output.isatty():
            raise OSError("No output TTY available")

        try:
            yield
        except OSError:
            raise
        except Exception as err:
            raise OSError(err) from err

    def xǁConsoleOutputǁask__mutmut_orig(self, prompt: str) -> str:
        with self._prompt():
            self._write_console(prompt)
            return input().strip()

    def xǁConsoleOutputǁask__mutmut_1(self, prompt: str) -> str:
        with self._prompt():
            self._write_console(None)
            return input().strip()
    
    xǁConsoleOutputǁask__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁask__mutmut_1': xǁConsoleOutputǁask__mutmut_1
    }
    
    def ask(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁask__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁask__mutmut_mutants"), args, kwargs, self)
        return result 
    
    ask.__signature__ = _mutmut_signature(xǁConsoleOutputǁask__mutmut_orig)
    xǁConsoleOutputǁask__mutmut_orig.__name__ = 'xǁConsoleOutputǁask'

    def xǁConsoleOutputǁask_password__mutmut_orig(self, prompt: str) -> str:
        with self._prompt():
            return getpass(prompt=prompt, stream=self._console_output)

    def xǁConsoleOutputǁask_password__mutmut_1(self, prompt: str) -> str:
        with self._prompt():
            return getpass(prompt=None, stream=self._console_output)

    def xǁConsoleOutputǁask_password__mutmut_2(self, prompt: str) -> str:
        with self._prompt():
            return getpass(prompt=prompt, stream=None)

    def xǁConsoleOutputǁask_password__mutmut_3(self, prompt: str) -> str:
        with self._prompt():
            return getpass(stream=self._console_output)

    def xǁConsoleOutputǁask_password__mutmut_4(self, prompt: str) -> str:
        with self._prompt():
            return getpass(prompt=prompt, )
    
    xǁConsoleOutputǁask_password__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁask_password__mutmut_1': xǁConsoleOutputǁask_password__mutmut_1, 
        'xǁConsoleOutputǁask_password__mutmut_2': xǁConsoleOutputǁask_password__mutmut_2, 
        'xǁConsoleOutputǁask_password__mutmut_3': xǁConsoleOutputǁask_password__mutmut_3, 
        'xǁConsoleOutputǁask_password__mutmut_4': xǁConsoleOutputǁask_password__mutmut_4
    }
    
    def ask_password(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁask_password__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁask_password__mutmut_mutants"), args, kwargs, self)
        return result 
    
    ask_password.__signature__ = _mutmut_signature(xǁConsoleOutputǁask_password__mutmut_orig)
    xǁConsoleOutputǁask_password__mutmut_orig.__name__ = 'xǁConsoleOutputǁask_password'

    def xǁConsoleOutputǁmsg__mutmut_orig(self, msg: str) -> None:
        if self.json:
            return
        msg = f"{msg}\n"
        self._write_console(msg)
        self._write_file(msg)

    def xǁConsoleOutputǁmsg__mutmut_1(self, msg: str) -> None:
        if self.json:
            return
        msg = None
        self._write_console(msg)
        self._write_file(msg)

    def xǁConsoleOutputǁmsg__mutmut_2(self, msg: str) -> None:
        if self.json:
            return
        msg = f"{msg}\n"
        self._write_console(None)
        self._write_file(msg)

    def xǁConsoleOutputǁmsg__mutmut_3(self, msg: str) -> None:
        if self.json:
            return
        msg = f"{msg}\n"
        self._write_console(msg)
        self._write_file(None)
    
    xǁConsoleOutputǁmsg__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁmsg__mutmut_1': xǁConsoleOutputǁmsg__mutmut_1, 
        'xǁConsoleOutputǁmsg__mutmut_2': xǁConsoleOutputǁmsg__mutmut_2, 
        'xǁConsoleOutputǁmsg__mutmut_3': xǁConsoleOutputǁmsg__mutmut_3
    }
    
    def msg(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁmsg__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁmsg__mutmut_mutants"), args, kwargs, self)
        return result 
    
    msg.__signature__ = _mutmut_signature(xǁConsoleOutputǁmsg__mutmut_orig)
    xǁConsoleOutputǁmsg__mutmut_orig.__name__ = 'xǁConsoleOutputǁmsg'

    def xǁConsoleOutputǁmsg_status__mutmut_orig(self, msg: str) -> None:
        if self.json or not self._supports_status_messages:
            return
        self._write_console(ConsoleStatusMessage(msg))

    def xǁConsoleOutputǁmsg_status__mutmut_1(self, msg: str) -> None:
        if self.json and not self._supports_status_messages:
            return
        self._write_console(ConsoleStatusMessage(msg))

    def xǁConsoleOutputǁmsg_status__mutmut_2(self, msg: str) -> None:
        if self.json or self._supports_status_messages:
            return
        self._write_console(ConsoleStatusMessage(msg))

    def xǁConsoleOutputǁmsg_status__mutmut_3(self, msg: str) -> None:
        if self.json or not self._supports_status_messages:
            return
        self._write_console(None)

    def xǁConsoleOutputǁmsg_status__mutmut_4(self, msg: str) -> None:
        if self.json or not self._supports_status_messages:
            return
        self._write_console(ConsoleStatusMessage(None))
    
    xǁConsoleOutputǁmsg_status__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁmsg_status__mutmut_1': xǁConsoleOutputǁmsg_status__mutmut_1, 
        'xǁConsoleOutputǁmsg_status__mutmut_2': xǁConsoleOutputǁmsg_status__mutmut_2, 
        'xǁConsoleOutputǁmsg_status__mutmut_3': xǁConsoleOutputǁmsg_status__mutmut_3, 
        'xǁConsoleOutputǁmsg_status__mutmut_4': xǁConsoleOutputǁmsg_status__mutmut_4
    }
    
    def msg_status(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁmsg_status__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁmsg_status__mutmut_mutants"), args, kwargs, self)
        return result 
    
    msg_status.__signature__ = _mutmut_signature(xǁConsoleOutputǁmsg_status__mutmut_orig)
    xǁConsoleOutputǁmsg_status__mutmut_orig.__name__ = 'xǁConsoleOutputǁmsg_status'

    def xǁConsoleOutputǁmsg_json__mutmut_orig(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_1(self, *objs: Any, **keywords: Any) -> None:
        if self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_2(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs or isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_3(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = None
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_4(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(None)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_5(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(None, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_6(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, None) and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_7(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr("__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_8(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, ) and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_9(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "XX__json__XX") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_10(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__JSON__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_11(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") or callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_12(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(None):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_13(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = None
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_14(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(None)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_15(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(None)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_16(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = None
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_17(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(None, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_18(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, None) and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_19(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr("__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_20(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, ) and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_21(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "XX__json__XX") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_22(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__JSON__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_23(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") or callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_24(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(None):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_25(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = None
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_26(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_27(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    break
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_28(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_29(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = None
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_30(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding == "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_31(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "XXutf-8XX"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_32(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "UTF-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_33(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "Utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_34(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = None
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_35(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(None, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_36(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=None, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_37(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=None, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_38(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=None)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_39(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_40(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_41(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_42(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, )
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_43(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=3)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_44(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(None)

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_45(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_46(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = None
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_47(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(None, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_48(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=None, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_49(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=None, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_50(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=None)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_51(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_52(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, ensure_ascii=False, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_53(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_54(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, )
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_55(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=True, indent=2)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_56(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=3)
            self._write(self._file_output, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_57(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(None, f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_58(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, None)

    def xǁConsoleOutputǁmsg_json__mutmut_59(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(f"{msg}\n")

    def xǁConsoleOutputǁmsg_json__mutmut_60(self, *objs: Any, **keywords: Any) -> None:
        if not self.json:
            return

        out: list | dict
        if objs and isinstance(objs[0], list):
            out = []
            for obj in objs:
                if isinstance(obj, list):
                    out.extend(obj)
                else:
                    if hasattr(obj, "__json__") and callable(obj.__json__):
                        obj = obj.__json__()
                    out.append(obj)
            if keywords:
                out.append(keywords)
        else:
            out = {}
            for obj in objs:
                if hasattr(obj, "__json__") and callable(obj.__json__):
                    obj = obj.__json__()
                if not isinstance(obj, dict):
                    continue
                out.update(**obj)
            out.update(**keywords)

        if self._console_output is not None:
            # don't escape Unicode characters outside the ASCII range if the output encoding is UTF-8
            ensure_ascii = self._console_output.encoding != "utf-8"
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=ensure_ascii, indent=2)
            self._write_console(f"{msg}\n")

        if self._file_output is not None:
            msg = dumps(out, cls=JSONEncoder, ensure_ascii=False, indent=2)
            self._write(self._file_output, )
    
    xǁConsoleOutputǁmsg_json__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁConsoleOutputǁmsg_json__mutmut_1': xǁConsoleOutputǁmsg_json__mutmut_1, 
        'xǁConsoleOutputǁmsg_json__mutmut_2': xǁConsoleOutputǁmsg_json__mutmut_2, 
        'xǁConsoleOutputǁmsg_json__mutmut_3': xǁConsoleOutputǁmsg_json__mutmut_3, 
        'xǁConsoleOutputǁmsg_json__mutmut_4': xǁConsoleOutputǁmsg_json__mutmut_4, 
        'xǁConsoleOutputǁmsg_json__mutmut_5': xǁConsoleOutputǁmsg_json__mutmut_5, 
        'xǁConsoleOutputǁmsg_json__mutmut_6': xǁConsoleOutputǁmsg_json__mutmut_6, 
        'xǁConsoleOutputǁmsg_json__mutmut_7': xǁConsoleOutputǁmsg_json__mutmut_7, 
        'xǁConsoleOutputǁmsg_json__mutmut_8': xǁConsoleOutputǁmsg_json__mutmut_8, 
        'xǁConsoleOutputǁmsg_json__mutmut_9': xǁConsoleOutputǁmsg_json__mutmut_9, 
        'xǁConsoleOutputǁmsg_json__mutmut_10': xǁConsoleOutputǁmsg_json__mutmut_10, 
        'xǁConsoleOutputǁmsg_json__mutmut_11': xǁConsoleOutputǁmsg_json__mutmut_11, 
        'xǁConsoleOutputǁmsg_json__mutmut_12': xǁConsoleOutputǁmsg_json__mutmut_12, 
        'xǁConsoleOutputǁmsg_json__mutmut_13': xǁConsoleOutputǁmsg_json__mutmut_13, 
        'xǁConsoleOutputǁmsg_json__mutmut_14': xǁConsoleOutputǁmsg_json__mutmut_14, 
        'xǁConsoleOutputǁmsg_json__mutmut_15': xǁConsoleOutputǁmsg_json__mutmut_15, 
        'xǁConsoleOutputǁmsg_json__mutmut_16': xǁConsoleOutputǁmsg_json__mutmut_16, 
        'xǁConsoleOutputǁmsg_json__mutmut_17': xǁConsoleOutputǁmsg_json__mutmut_17, 
        'xǁConsoleOutputǁmsg_json__mutmut_18': xǁConsoleOutputǁmsg_json__mutmut_18, 
        'xǁConsoleOutputǁmsg_json__mutmut_19': xǁConsoleOutputǁmsg_json__mutmut_19, 
        'xǁConsoleOutputǁmsg_json__mutmut_20': xǁConsoleOutputǁmsg_json__mutmut_20, 
        'xǁConsoleOutputǁmsg_json__mutmut_21': xǁConsoleOutputǁmsg_json__mutmut_21, 
        'xǁConsoleOutputǁmsg_json__mutmut_22': xǁConsoleOutputǁmsg_json__mutmut_22, 
        'xǁConsoleOutputǁmsg_json__mutmut_23': xǁConsoleOutputǁmsg_json__mutmut_23, 
        'xǁConsoleOutputǁmsg_json__mutmut_24': xǁConsoleOutputǁmsg_json__mutmut_24, 
        'xǁConsoleOutputǁmsg_json__mutmut_25': xǁConsoleOutputǁmsg_json__mutmut_25, 
        'xǁConsoleOutputǁmsg_json__mutmut_26': xǁConsoleOutputǁmsg_json__mutmut_26, 
        'xǁConsoleOutputǁmsg_json__mutmut_27': xǁConsoleOutputǁmsg_json__mutmut_27, 
        'xǁConsoleOutputǁmsg_json__mutmut_28': xǁConsoleOutputǁmsg_json__mutmut_28, 
        'xǁConsoleOutputǁmsg_json__mutmut_29': xǁConsoleOutputǁmsg_json__mutmut_29, 
        'xǁConsoleOutputǁmsg_json__mutmut_30': xǁConsoleOutputǁmsg_json__mutmut_30, 
        'xǁConsoleOutputǁmsg_json__mutmut_31': xǁConsoleOutputǁmsg_json__mutmut_31, 
        'xǁConsoleOutputǁmsg_json__mutmut_32': xǁConsoleOutputǁmsg_json__mutmut_32, 
        'xǁConsoleOutputǁmsg_json__mutmut_33': xǁConsoleOutputǁmsg_json__mutmut_33, 
        'xǁConsoleOutputǁmsg_json__mutmut_34': xǁConsoleOutputǁmsg_json__mutmut_34, 
        'xǁConsoleOutputǁmsg_json__mutmut_35': xǁConsoleOutputǁmsg_json__mutmut_35, 
        'xǁConsoleOutputǁmsg_json__mutmut_36': xǁConsoleOutputǁmsg_json__mutmut_36, 
        'xǁConsoleOutputǁmsg_json__mutmut_37': xǁConsoleOutputǁmsg_json__mutmut_37, 
        'xǁConsoleOutputǁmsg_json__mutmut_38': xǁConsoleOutputǁmsg_json__mutmut_38, 
        'xǁConsoleOutputǁmsg_json__mutmut_39': xǁConsoleOutputǁmsg_json__mutmut_39, 
        'xǁConsoleOutputǁmsg_json__mutmut_40': xǁConsoleOutputǁmsg_json__mutmut_40, 
        'xǁConsoleOutputǁmsg_json__mutmut_41': xǁConsoleOutputǁmsg_json__mutmut_41, 
        'xǁConsoleOutputǁmsg_json__mutmut_42': xǁConsoleOutputǁmsg_json__mutmut_42, 
        'xǁConsoleOutputǁmsg_json__mutmut_43': xǁConsoleOutputǁmsg_json__mutmut_43, 
        'xǁConsoleOutputǁmsg_json__mutmut_44': xǁConsoleOutputǁmsg_json__mutmut_44, 
        'xǁConsoleOutputǁmsg_json__mutmut_45': xǁConsoleOutputǁmsg_json__mutmut_45, 
        'xǁConsoleOutputǁmsg_json__mutmut_46': xǁConsoleOutputǁmsg_json__mutmut_46, 
        'xǁConsoleOutputǁmsg_json__mutmut_47': xǁConsoleOutputǁmsg_json__mutmut_47, 
        'xǁConsoleOutputǁmsg_json__mutmut_48': xǁConsoleOutputǁmsg_json__mutmut_48, 
        'xǁConsoleOutputǁmsg_json__mutmut_49': xǁConsoleOutputǁmsg_json__mutmut_49, 
        'xǁConsoleOutputǁmsg_json__mutmut_50': xǁConsoleOutputǁmsg_json__mutmut_50, 
        'xǁConsoleOutputǁmsg_json__mutmut_51': xǁConsoleOutputǁmsg_json__mutmut_51, 
        'xǁConsoleOutputǁmsg_json__mutmut_52': xǁConsoleOutputǁmsg_json__mutmut_52, 
        'xǁConsoleOutputǁmsg_json__mutmut_53': xǁConsoleOutputǁmsg_json__mutmut_53, 
        'xǁConsoleOutputǁmsg_json__mutmut_54': xǁConsoleOutputǁmsg_json__mutmut_54, 
        'xǁConsoleOutputǁmsg_json__mutmut_55': xǁConsoleOutputǁmsg_json__mutmut_55, 
        'xǁConsoleOutputǁmsg_json__mutmut_56': xǁConsoleOutputǁmsg_json__mutmut_56, 
        'xǁConsoleOutputǁmsg_json__mutmut_57': xǁConsoleOutputǁmsg_json__mutmut_57, 
        'xǁConsoleOutputǁmsg_json__mutmut_58': xǁConsoleOutputǁmsg_json__mutmut_58, 
        'xǁConsoleOutputǁmsg_json__mutmut_59': xǁConsoleOutputǁmsg_json__mutmut_59, 
        'xǁConsoleOutputǁmsg_json__mutmut_60': xǁConsoleOutputǁmsg_json__mutmut_60
    }
    
    def msg_json(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁConsoleOutputǁmsg_json__mutmut_orig"), object.__getattribute__(self, "xǁConsoleOutputǁmsg_json__mutmut_mutants"), args, kwargs, self)
        return result 
    
    msg_json.__signature__ = _mutmut_signature(xǁConsoleOutputǁmsg_json__mutmut_orig)
    xǁConsoleOutputǁmsg_json__mutmut_orig.__name__ = 'xǁConsoleOutputǁmsg_json'

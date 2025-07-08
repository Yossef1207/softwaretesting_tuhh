from __future__ import annotations

import logging
import os
import re
import shlex
import subprocess
import sys
import warnings
from collections.abc import Mapping, Sequence
from contextlib import suppress
from pathlib import Path
from shutil import which
from time import sleep
from typing import ClassVar, TextIO

from streamlink.compat import is_win32
from streamlink.exceptions import StreamlinkWarning
from streamlink.utils.named_pipe import NamedPipeBase
from streamlink_cli.output.abc import Output
from streamlink_cli.output.file import FileOutput
from streamlink_cli.output.http import HTTPOutput
from streamlink_cli.utils import Formatter


log = logging.getLogger("streamlink.cli.output")
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


class PlayerArgs:
    EXECUTABLES: ClassVar[list[re.Pattern]] = []

    def xǁPlayerArgsǁ__init____mutmut_orig(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_1(
        self,
        path: Path,
        args: str = "XXXX",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_2(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = None
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_3(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = None
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_4(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = None

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_5(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = None
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_6(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" not in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_7(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = None

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_8(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" not in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_9(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = None
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_10(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(None)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_11(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = None
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_12(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(None)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_13(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = None
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_14(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(None)
        else:
            self._input = self.get_stdin()

    def xǁPlayerArgsǁ__init____mutmut_15(
        self,
        path: Path,
        args: str = "",
        title: str | None = None,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
    ):
        self.path = path
        self.args = args
        self.title = title

        self._has_var_playerinput = f"{{{PlayerOutput.PLAYER_ARGS_INPUT}}}" in args
        self._has_var_playertitleargs = f"{{{PlayerOutput.PLAYER_ARGS_TITLE}}}" in args

        if namedpipe:
            self._input = self.get_namedpipe(namedpipe)
        elif filename:
            self._input = self.get_filename(filename)
        elif http:
            self._input = self.get_http(http)
        else:
            self._input = None
    
    xǁPlayerArgsǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsǁ__init____mutmut_1': xǁPlayerArgsǁ__init____mutmut_1, 
        'xǁPlayerArgsǁ__init____mutmut_2': xǁPlayerArgsǁ__init____mutmut_2, 
        'xǁPlayerArgsǁ__init____mutmut_3': xǁPlayerArgsǁ__init____mutmut_3, 
        'xǁPlayerArgsǁ__init____mutmut_4': xǁPlayerArgsǁ__init____mutmut_4, 
        'xǁPlayerArgsǁ__init____mutmut_5': xǁPlayerArgsǁ__init____mutmut_5, 
        'xǁPlayerArgsǁ__init____mutmut_6': xǁPlayerArgsǁ__init____mutmut_6, 
        'xǁPlayerArgsǁ__init____mutmut_7': xǁPlayerArgsǁ__init____mutmut_7, 
        'xǁPlayerArgsǁ__init____mutmut_8': xǁPlayerArgsǁ__init____mutmut_8, 
        'xǁPlayerArgsǁ__init____mutmut_9': xǁPlayerArgsǁ__init____mutmut_9, 
        'xǁPlayerArgsǁ__init____mutmut_10': xǁPlayerArgsǁ__init____mutmut_10, 
        'xǁPlayerArgsǁ__init____mutmut_11': xǁPlayerArgsǁ__init____mutmut_11, 
        'xǁPlayerArgsǁ__init____mutmut_12': xǁPlayerArgsǁ__init____mutmut_12, 
        'xǁPlayerArgsǁ__init____mutmut_13': xǁPlayerArgsǁ__init____mutmut_13, 
        'xǁPlayerArgsǁ__init____mutmut_14': xǁPlayerArgsǁ__init____mutmut_14, 
        'xǁPlayerArgsǁ__init____mutmut_15': xǁPlayerArgsǁ__init____mutmut_15
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPlayerArgsǁ__init____mutmut_orig)
    xǁPlayerArgsǁ__init____mutmut_orig.__name__ = 'xǁPlayerArgsǁ__init__'

    def xǁPlayerArgsǁbuild__mutmut_orig(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_1(self) -> list[str]:
        args_title = None
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_2(self) -> list[str]:
        args_title = []
        if self.title is None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_3(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(None)

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_4(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(None))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_5(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = None
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_6(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter(None)
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_7(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: None,
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_8(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline(None),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_9(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: None,
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_10(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(None),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_11(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = None
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_12(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(None)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_13(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = None

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_14(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(None)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_15(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.rsplit(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_16(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_17(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = None
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_18(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_19(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(None)

        return [str(self.path), *args_tokenized]

    def xǁPlayerArgsǁbuild__mutmut_20(self) -> list[str]:
        args_title = []
        if self.title is not None:
            args_title.extend(self.get_title(self.title))

        # format args via the formatter, so that invalid/unknown variables don't raise a KeyError
        argsformatter = Formatter({
            PlayerOutput.PLAYER_ARGS_INPUT: lambda: subprocess.list2cmdline([self._input]),
            PlayerOutput.PLAYER_ARGS_TITLE: lambda: subprocess.list2cmdline(args_title),
        })
        args = argsformatter.title(self.args)
        args_tokenized = shlex.split(args)

        if not self._has_var_playertitleargs:
            args_tokenized = [*args_title, *args_tokenized]
        if not self._has_var_playerinput:
            args_tokenized.append(self._input)

        return [str(None), *args_tokenized]
    
    xǁPlayerArgsǁbuild__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsǁbuild__mutmut_1': xǁPlayerArgsǁbuild__mutmut_1, 
        'xǁPlayerArgsǁbuild__mutmut_2': xǁPlayerArgsǁbuild__mutmut_2, 
        'xǁPlayerArgsǁbuild__mutmut_3': xǁPlayerArgsǁbuild__mutmut_3, 
        'xǁPlayerArgsǁbuild__mutmut_4': xǁPlayerArgsǁbuild__mutmut_4, 
        'xǁPlayerArgsǁbuild__mutmut_5': xǁPlayerArgsǁbuild__mutmut_5, 
        'xǁPlayerArgsǁbuild__mutmut_6': xǁPlayerArgsǁbuild__mutmut_6, 
        'xǁPlayerArgsǁbuild__mutmut_7': xǁPlayerArgsǁbuild__mutmut_7, 
        'xǁPlayerArgsǁbuild__mutmut_8': xǁPlayerArgsǁbuild__mutmut_8, 
        'xǁPlayerArgsǁbuild__mutmut_9': xǁPlayerArgsǁbuild__mutmut_9, 
        'xǁPlayerArgsǁbuild__mutmut_10': xǁPlayerArgsǁbuild__mutmut_10, 
        'xǁPlayerArgsǁbuild__mutmut_11': xǁPlayerArgsǁbuild__mutmut_11, 
        'xǁPlayerArgsǁbuild__mutmut_12': xǁPlayerArgsǁbuild__mutmut_12, 
        'xǁPlayerArgsǁbuild__mutmut_13': xǁPlayerArgsǁbuild__mutmut_13, 
        'xǁPlayerArgsǁbuild__mutmut_14': xǁPlayerArgsǁbuild__mutmut_14, 
        'xǁPlayerArgsǁbuild__mutmut_15': xǁPlayerArgsǁbuild__mutmut_15, 
        'xǁPlayerArgsǁbuild__mutmut_16': xǁPlayerArgsǁbuild__mutmut_16, 
        'xǁPlayerArgsǁbuild__mutmut_17': xǁPlayerArgsǁbuild__mutmut_17, 
        'xǁPlayerArgsǁbuild__mutmut_18': xǁPlayerArgsǁbuild__mutmut_18, 
        'xǁPlayerArgsǁbuild__mutmut_19': xǁPlayerArgsǁbuild__mutmut_19, 
        'xǁPlayerArgsǁbuild__mutmut_20': xǁPlayerArgsǁbuild__mutmut_20
    }
    
    def build(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsǁbuild__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsǁbuild__mutmut_mutants"), args, kwargs, self)
        return result 
    
    build.__signature__ = _mutmut_signature(xǁPlayerArgsǁbuild__mutmut_orig)
    xǁPlayerArgsǁbuild__mutmut_orig.__name__ = 'xǁPlayerArgsǁbuild'

    # noinspection PyMethodMayBeStatic
    def xǁPlayerArgsǁget_stdin__mutmut_orig(self) -> str:
        return "-"

    # noinspection PyMethodMayBeStatic
    def xǁPlayerArgsǁget_stdin__mutmut_1(self) -> str:
        return "XX-XX"
    
    xǁPlayerArgsǁget_stdin__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsǁget_stdin__mutmut_1': xǁPlayerArgsǁget_stdin__mutmut_1
    }
    
    def get_stdin(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsǁget_stdin__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsǁget_stdin__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_stdin.__signature__ = _mutmut_signature(xǁPlayerArgsǁget_stdin__mutmut_orig)
    xǁPlayerArgsǁget_stdin__mutmut_orig.__name__ = 'xǁPlayerArgsǁget_stdin'

    def xǁPlayerArgsǁget_namedpipe__mutmut_orig(self, namedpipe: NamedPipeBase) -> str:
        return str(namedpipe.path)

    def xǁPlayerArgsǁget_namedpipe__mutmut_1(self, namedpipe: NamedPipeBase) -> str:
        return str(None)
    
    xǁPlayerArgsǁget_namedpipe__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsǁget_namedpipe__mutmut_1': xǁPlayerArgsǁget_namedpipe__mutmut_1
    }
    
    def get_namedpipe(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsǁget_namedpipe__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsǁget_namedpipe__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_namedpipe.__signature__ = _mutmut_signature(xǁPlayerArgsǁget_namedpipe__mutmut_orig)
    xǁPlayerArgsǁget_namedpipe__mutmut_orig.__name__ = 'xǁPlayerArgsǁget_namedpipe'

    # noinspection PyMethodMayBeStatic
    def get_filename(self, filename: str) -> str:
        return filename

    # noinspection PyMethodMayBeStatic
    def get_http(self, http: HTTPOutput) -> str:
        return http.url

    def get_title(self, title: str) -> list[str]:
        return []


class PlayerArgsVLC(PlayerArgs):
    EXECUTABLES: ClassVar[list[re.Pattern]] = [
        re.compile(r"^vlc$", re.IGNORECASE),
    ]

    def xǁPlayerArgsVLCǁget_namedpipe__mutmut_orig(self, namedpipe: NamedPipeBase) -> str:
        if is_win32:
            return f"stream://\\{namedpipe.path}"

        return super().get_namedpipe(namedpipe)

    def xǁPlayerArgsVLCǁget_namedpipe__mutmut_1(self, namedpipe: NamedPipeBase) -> str:
        if is_win32:
            return f"stream://\\{namedpipe.path}"

        return super().get_namedpipe(None)
    
    xǁPlayerArgsVLCǁget_namedpipe__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsVLCǁget_namedpipe__mutmut_1': xǁPlayerArgsVLCǁget_namedpipe__mutmut_1
    }
    
    def get_namedpipe(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsVLCǁget_namedpipe__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsVLCǁget_namedpipe__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_namedpipe.__signature__ = _mutmut_signature(xǁPlayerArgsVLCǁget_namedpipe__mutmut_orig)
    xǁPlayerArgsVLCǁget_namedpipe__mutmut_orig.__name__ = 'xǁPlayerArgsVLCǁget_namedpipe'

    def xǁPlayerArgsVLCǁget_title__mutmut_orig(self, title) -> list[str]:
        title = title.replace("$", "$$")

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_1(self, title) -> list[str]:
        title = None

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_2(self, title) -> list[str]:
        title = title.replace(None, "$$")

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_3(self, title) -> list[str]:
        title = title.replace("$", None)

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_4(self, title) -> list[str]:
        title = title.replace("$$")

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_5(self, title) -> list[str]:
        title = title.replace("$", )

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_6(self, title) -> list[str]:
        title = title.replace("XX$XX", "$$")

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_7(self, title) -> list[str]:
        title = title.replace("$", "XX$$XX")

        return ["--input-title-format", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_8(self, title) -> list[str]:
        title = title.replace("$", "$$")

        return ["XX--input-title-formatXX", title]

    def xǁPlayerArgsVLCǁget_title__mutmut_9(self, title) -> list[str]:
        title = title.replace("$", "$$")

        return ["--INPUT-TITLE-FORMAT", title]
    
    xǁPlayerArgsVLCǁget_title__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsVLCǁget_title__mutmut_1': xǁPlayerArgsVLCǁget_title__mutmut_1, 
        'xǁPlayerArgsVLCǁget_title__mutmut_2': xǁPlayerArgsVLCǁget_title__mutmut_2, 
        'xǁPlayerArgsVLCǁget_title__mutmut_3': xǁPlayerArgsVLCǁget_title__mutmut_3, 
        'xǁPlayerArgsVLCǁget_title__mutmut_4': xǁPlayerArgsVLCǁget_title__mutmut_4, 
        'xǁPlayerArgsVLCǁget_title__mutmut_5': xǁPlayerArgsVLCǁget_title__mutmut_5, 
        'xǁPlayerArgsVLCǁget_title__mutmut_6': xǁPlayerArgsVLCǁget_title__mutmut_6, 
        'xǁPlayerArgsVLCǁget_title__mutmut_7': xǁPlayerArgsVLCǁget_title__mutmut_7, 
        'xǁPlayerArgsVLCǁget_title__mutmut_8': xǁPlayerArgsVLCǁget_title__mutmut_8, 
        'xǁPlayerArgsVLCǁget_title__mutmut_9': xǁPlayerArgsVLCǁget_title__mutmut_9
    }
    
    def get_title(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsVLCǁget_title__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsVLCǁget_title__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_title.__signature__ = _mutmut_signature(xǁPlayerArgsVLCǁget_title__mutmut_orig)
    xǁPlayerArgsVLCǁget_title__mutmut_orig.__name__ = 'xǁPlayerArgsVLCǁget_title'


class PlayerArgsMPV(PlayerArgs):
    EXECUTABLES: ClassVar[list[re.Pattern]] = [
        re.compile(r"^mpv$", re.IGNORECASE),
    ]

    def xǁPlayerArgsMPVǁget_namedpipe__mutmut_orig(self, namedpipe: NamedPipeBase) -> str:
        if is_win32:
            return f"file://{namedpipe.path}"

        return super().get_namedpipe(namedpipe)

    def xǁPlayerArgsMPVǁget_namedpipe__mutmut_1(self, namedpipe: NamedPipeBase) -> str:
        if is_win32:
            return f"file://{namedpipe.path}"

        return super().get_namedpipe(None)
    
    xǁPlayerArgsMPVǁget_namedpipe__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsMPVǁget_namedpipe__mutmut_1': xǁPlayerArgsMPVǁget_namedpipe__mutmut_1
    }
    
    def get_namedpipe(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsMPVǁget_namedpipe__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsMPVǁget_namedpipe__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_namedpipe.__signature__ = _mutmut_signature(xǁPlayerArgsMPVǁget_namedpipe__mutmut_orig)
    xǁPlayerArgsMPVǁget_namedpipe__mutmut_orig.__name__ = 'xǁPlayerArgsMPVǁget_namedpipe'

    def get_title(self, title: str) -> list[str]:
        return [f"--force-media-title={title}"]


class PlayerArgsPotplayer(PlayerArgs):
    EXECUTABLES: ClassVar[list[re.Pattern]] = [
        re.compile(r"^potplayer(?:mini(?:64)?)?$", re.IGNORECASE),
    ]

    def xǁPlayerArgsPotplayerǁget_title__mutmut_orig(self, title: str) -> list[str]:
        if self._input != "-":
            # PotPlayer CLI help:
            # "You can specify titles for URLs by separating them with a backslash (\) at the end of URLs."
            self._input = f"{self._input}\\{title}"

        return []

    def xǁPlayerArgsPotplayerǁget_title__mutmut_1(self, title: str) -> list[str]:
        if self._input == "-":
            # PotPlayer CLI help:
            # "You can specify titles for URLs by separating them with a backslash (\) at the end of URLs."
            self._input = f"{self._input}\\{title}"

        return []

    def xǁPlayerArgsPotplayerǁget_title__mutmut_2(self, title: str) -> list[str]:
        if self._input != "XX-XX":
            # PotPlayer CLI help:
            # "You can specify titles for URLs by separating them with a backslash (\) at the end of URLs."
            self._input = f"{self._input}\\{title}"

        return []

    def xǁPlayerArgsPotplayerǁget_title__mutmut_3(self, title: str) -> list[str]:
        if self._input != "-":
            # PotPlayer CLI help:
            # "You can specify titles for URLs by separating them with a backslash (\) at the end of URLs."
            self._input = None

        return []
    
    xǁPlayerArgsPotplayerǁget_title__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerArgsPotplayerǁget_title__mutmut_1': xǁPlayerArgsPotplayerǁget_title__mutmut_1, 
        'xǁPlayerArgsPotplayerǁget_title__mutmut_2': xǁPlayerArgsPotplayerǁget_title__mutmut_2, 
        'xǁPlayerArgsPotplayerǁget_title__mutmut_3': xǁPlayerArgsPotplayerǁget_title__mutmut_3
    }
    
    def get_title(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerArgsPotplayerǁget_title__mutmut_orig"), object.__getattribute__(self, "xǁPlayerArgsPotplayerǁget_title__mutmut_mutants"), args, kwargs, self)
        return result 
    
    get_title.__signature__ = _mutmut_signature(xǁPlayerArgsPotplayerǁget_title__mutmut_orig)
    xǁPlayerArgsPotplayerǁget_title__mutmut_orig.__name__ = 'xǁPlayerArgsPotplayerǁget_title'


class PlayerOutput(Output):
    PLAYER_TERMINATE_TIMEOUT = 10.0

    PLAYER_ARGS_INPUT = "playerinput"
    PLAYER_ARGS_TITLE = "playertitleargs"

    PLAYERS: ClassVar[Mapping[str, type[PlayerArgs]]] = {
        "vlc": PlayerArgsVLC,
        "mpv": PlayerArgsMPV,
        "potplayer": PlayerArgsPotplayer,
    }

    player: subprocess.Popen
    stdin: int | TextIO
    stdout: int | TextIO
    stderr: int | TextIO

    def xǁPlayerOutputǁ__init____mutmut_orig(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_1(
        self,
        path: Path,
        args: str = "XXXX",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_2(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = False,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_3(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = False,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_4(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = True,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_5(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = None
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_6(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = None
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_7(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = None

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_8(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(None)

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_9(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env and {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_10(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = None
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_11(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = None
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_12(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = None

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_13(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = None
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_14(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = None
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_15(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = None
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_16(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = None

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_17(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = None

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_18(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = None

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_19(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=None,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_20(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=None,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_21(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=None,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_22(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=None,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_23(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=None,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_24(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=None,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_25(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_26(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_27(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_28(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_29(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_30(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_31(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe and self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_32(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename and self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_33(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = None
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_34(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = None

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_35(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = None
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_36(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = None
        else:
            self.stdout = sys.stdout
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_37(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = None
            self.stderr = sys.stderr

    def xǁPlayerOutputǁ__init____mutmut_38(
        self,
        path: Path,
        args: str = "",
        env: Sequence[tuple[str, str]] | None = None,
        quiet: bool = True,
        kill: bool = True,
        call: bool = False,
        filename: str | None = None,
        namedpipe: NamedPipeBase | None = None,
        http: HTTPOutput | None = None,
        record: FileOutput | None = None,
        title: str | None = None,
    ):
        super().__init__()

        self.path = path
        self.args = args
        self.env: Mapping[str, str] = dict(env or {})

        self.kill = kill
        self.call = call
        self.quiet = quiet

        self.filename = filename
        self.namedpipe = namedpipe
        self.http = http
        self.record = record

        self.title = title

        self.playerargs = self.playerargsfactory(
            path=path,
            args=args,
            title=title,
            namedpipe=namedpipe,
            filename=filename,
            http=http,
        )

        if self.namedpipe or self.filename or self.http:
            self.stdin = sys.stdin
        else:
            self.stdin = subprocess.PIPE

        if self.quiet:
            self.stdout = subprocess.DEVNULL
            self.stderr = subprocess.DEVNULL
        else:
            self.stdout = sys.stdout
            self.stderr = None
    
    xǁPlayerOutputǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ__init____mutmut_1': xǁPlayerOutputǁ__init____mutmut_1, 
        'xǁPlayerOutputǁ__init____mutmut_2': xǁPlayerOutputǁ__init____mutmut_2, 
        'xǁPlayerOutputǁ__init____mutmut_3': xǁPlayerOutputǁ__init____mutmut_3, 
        'xǁPlayerOutputǁ__init____mutmut_4': xǁPlayerOutputǁ__init____mutmut_4, 
        'xǁPlayerOutputǁ__init____mutmut_5': xǁPlayerOutputǁ__init____mutmut_5, 
        'xǁPlayerOutputǁ__init____mutmut_6': xǁPlayerOutputǁ__init____mutmut_6, 
        'xǁPlayerOutputǁ__init____mutmut_7': xǁPlayerOutputǁ__init____mutmut_7, 
        'xǁPlayerOutputǁ__init____mutmut_8': xǁPlayerOutputǁ__init____mutmut_8, 
        'xǁPlayerOutputǁ__init____mutmut_9': xǁPlayerOutputǁ__init____mutmut_9, 
        'xǁPlayerOutputǁ__init____mutmut_10': xǁPlayerOutputǁ__init____mutmut_10, 
        'xǁPlayerOutputǁ__init____mutmut_11': xǁPlayerOutputǁ__init____mutmut_11, 
        'xǁPlayerOutputǁ__init____mutmut_12': xǁPlayerOutputǁ__init____mutmut_12, 
        'xǁPlayerOutputǁ__init____mutmut_13': xǁPlayerOutputǁ__init____mutmut_13, 
        'xǁPlayerOutputǁ__init____mutmut_14': xǁPlayerOutputǁ__init____mutmut_14, 
        'xǁPlayerOutputǁ__init____mutmut_15': xǁPlayerOutputǁ__init____mutmut_15, 
        'xǁPlayerOutputǁ__init____mutmut_16': xǁPlayerOutputǁ__init____mutmut_16, 
        'xǁPlayerOutputǁ__init____mutmut_17': xǁPlayerOutputǁ__init____mutmut_17, 
        'xǁPlayerOutputǁ__init____mutmut_18': xǁPlayerOutputǁ__init____mutmut_18, 
        'xǁPlayerOutputǁ__init____mutmut_19': xǁPlayerOutputǁ__init____mutmut_19, 
        'xǁPlayerOutputǁ__init____mutmut_20': xǁPlayerOutputǁ__init____mutmut_20, 
        'xǁPlayerOutputǁ__init____mutmut_21': xǁPlayerOutputǁ__init____mutmut_21, 
        'xǁPlayerOutputǁ__init____mutmut_22': xǁPlayerOutputǁ__init____mutmut_22, 
        'xǁPlayerOutputǁ__init____mutmut_23': xǁPlayerOutputǁ__init____mutmut_23, 
        'xǁPlayerOutputǁ__init____mutmut_24': xǁPlayerOutputǁ__init____mutmut_24, 
        'xǁPlayerOutputǁ__init____mutmut_25': xǁPlayerOutputǁ__init____mutmut_25, 
        'xǁPlayerOutputǁ__init____mutmut_26': xǁPlayerOutputǁ__init____mutmut_26, 
        'xǁPlayerOutputǁ__init____mutmut_27': xǁPlayerOutputǁ__init____mutmut_27, 
        'xǁPlayerOutputǁ__init____mutmut_28': xǁPlayerOutputǁ__init____mutmut_28, 
        'xǁPlayerOutputǁ__init____mutmut_29': xǁPlayerOutputǁ__init____mutmut_29, 
        'xǁPlayerOutputǁ__init____mutmut_30': xǁPlayerOutputǁ__init____mutmut_30, 
        'xǁPlayerOutputǁ__init____mutmut_31': xǁPlayerOutputǁ__init____mutmut_31, 
        'xǁPlayerOutputǁ__init____mutmut_32': xǁPlayerOutputǁ__init____mutmut_32, 
        'xǁPlayerOutputǁ__init____mutmut_33': xǁPlayerOutputǁ__init____mutmut_33, 
        'xǁPlayerOutputǁ__init____mutmut_34': xǁPlayerOutputǁ__init____mutmut_34, 
        'xǁPlayerOutputǁ__init____mutmut_35': xǁPlayerOutputǁ__init____mutmut_35, 
        'xǁPlayerOutputǁ__init____mutmut_36': xǁPlayerOutputǁ__init____mutmut_36, 
        'xǁPlayerOutputǁ__init____mutmut_37': xǁPlayerOutputǁ__init____mutmut_37, 
        'xǁPlayerOutputǁ__init____mutmut_38': xǁPlayerOutputǁ__init____mutmut_38
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁPlayerOutputǁ__init____mutmut_orig)
    xǁPlayerOutputǁ__init____mutmut_orig.__name__ = 'xǁPlayerOutputǁ__init__'

    @classmethod
    def playerargsfactory(cls, path: Path, **kwargs) -> PlayerArgs:
        executable = path.name
        if is_win32 and executable[-4:].lower() == ".exe":
            executable = executable[:-4]

        for playerclass in cls.PLAYERS.values():
            for re_executable in playerclass.EXECUTABLES:
                if re_executable.search(executable):
                    return playerclass(path=path, **kwargs)

        return PlayerArgs(path=path, **kwargs)

    @property
    def running(self):
        sleep(0.5)
        return self.player.poll() is None

    def xǁPlayerOutputǁ_open__mutmut_orig(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_1(self):
        args = None

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_2(self):
        args = self.playerargs.build()

        playerpath = None
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_3(self):
        args = self.playerargs.build()

        playerpath = args[1]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_4(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = None
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_5(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[1] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_6(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(None)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_7(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_8(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[1]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_9(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:2] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_10(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] not in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_11(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('XX"XX', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_12(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "XX'XX"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_13(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    None,
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_14(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    None,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_15(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=None,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_16(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_17(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_18(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_19(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join(None),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_20(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "XX\nXX".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_21(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\N".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_22(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "XXThe --player argument has been changed and now only takes player path values:XX",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_23(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "the --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_24(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "THE --PLAYER ARGUMENT HAS BEEN CHANGED AND NOW ONLY TAKES PLAYER PATH VALUES:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_25(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "XX  Player paths must not be wrapped in additional quotation marksXX",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_26(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_27(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  PLAYER PATHS MUST NOT BE WRAPPED IN ADDITIONAL QUOTATION MARKS",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_28(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_29(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "XX  and custom player arguments need to be set via --player-args.XX",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_30(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  AND CUSTOM PLAYER ARGUMENTS NEED TO BE SET VIA --PLAYER-ARGS.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_31(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "XX  This is most likely caused by using an old config file from an ealier Streamlink version.XX",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_32(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  this is most likely caused by using an old config file from an ealier streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_33(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  THIS IS MOST LIKELY CAUSED BY USING AN OLD CONFIG FILE FROM AN EALIER STREAMLINK VERSION.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_34(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  this is most likely caused by using an old config file from an ealier streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_35(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "XX  Please see the migration guides in Streamlink's documentation:XX",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_36(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  please see the migration guides in streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_37(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  PLEASE SEE THE MIGRATION GUIDES IN STREAMLINK'S DOCUMENTATION:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_38(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  please see the migration guides in streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_39(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "XX  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argumentXX",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_40(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  HTTPS://STREAMLINK.GITHUB.IO/MIGRATIONS.HTML#PLAYER-PATH-ONLY-PLAYER-CLI-ARGUMENT",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_41(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=2,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_42(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError(None)

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_43(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("XXPlayer executable not foundXX")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_44(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_45(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("PLAYER EXECUTABLE NOT FOUND")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_46(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call or self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_47(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(None)
        else:
            self._open_subprocess(args)

    def xǁPlayerOutputǁ_open__mutmut_48(self):
        args = self.playerargs.build()

        playerpath = args[0]
        args[0] = which(playerpath)
        if not args[0]:
            if playerpath[:1] in ('"', "'"):
                warnings.warn(
                    "\n".join([
                        "The --player argument has been changed and now only takes player path values:",
                        "  Player paths must not be wrapped in additional quotation marks",
                        "  and custom player arguments need to be set via --player-args.",
                        "  This is most likely caused by using an old config file from an ealier Streamlink version.",
                        "  Please see the migration guides in Streamlink's documentation:",
                        "  https://streamlink.github.io/migrations.html#player-path-only-player-cli-argument",
                    ]),
                    StreamlinkWarning,
                    stacklevel=1,
                )

            raise FileNotFoundError("Player executable not found")

        if self.record:
            self.record.open()
        if self.call and self.filename:
            self._open_call(args)
        else:
            self._open_subprocess(None)
    
    xǁPlayerOutputǁ_open__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ_open__mutmut_1': xǁPlayerOutputǁ_open__mutmut_1, 
        'xǁPlayerOutputǁ_open__mutmut_2': xǁPlayerOutputǁ_open__mutmut_2, 
        'xǁPlayerOutputǁ_open__mutmut_3': xǁPlayerOutputǁ_open__mutmut_3, 
        'xǁPlayerOutputǁ_open__mutmut_4': xǁPlayerOutputǁ_open__mutmut_4, 
        'xǁPlayerOutputǁ_open__mutmut_5': xǁPlayerOutputǁ_open__mutmut_5, 
        'xǁPlayerOutputǁ_open__mutmut_6': xǁPlayerOutputǁ_open__mutmut_6, 
        'xǁPlayerOutputǁ_open__mutmut_7': xǁPlayerOutputǁ_open__mutmut_7, 
        'xǁPlayerOutputǁ_open__mutmut_8': xǁPlayerOutputǁ_open__mutmut_8, 
        'xǁPlayerOutputǁ_open__mutmut_9': xǁPlayerOutputǁ_open__mutmut_9, 
        'xǁPlayerOutputǁ_open__mutmut_10': xǁPlayerOutputǁ_open__mutmut_10, 
        'xǁPlayerOutputǁ_open__mutmut_11': xǁPlayerOutputǁ_open__mutmut_11, 
        'xǁPlayerOutputǁ_open__mutmut_12': xǁPlayerOutputǁ_open__mutmut_12, 
        'xǁPlayerOutputǁ_open__mutmut_13': xǁPlayerOutputǁ_open__mutmut_13, 
        'xǁPlayerOutputǁ_open__mutmut_14': xǁPlayerOutputǁ_open__mutmut_14, 
        'xǁPlayerOutputǁ_open__mutmut_15': xǁPlayerOutputǁ_open__mutmut_15, 
        'xǁPlayerOutputǁ_open__mutmut_16': xǁPlayerOutputǁ_open__mutmut_16, 
        'xǁPlayerOutputǁ_open__mutmut_17': xǁPlayerOutputǁ_open__mutmut_17, 
        'xǁPlayerOutputǁ_open__mutmut_18': xǁPlayerOutputǁ_open__mutmut_18, 
        'xǁPlayerOutputǁ_open__mutmut_19': xǁPlayerOutputǁ_open__mutmut_19, 
        'xǁPlayerOutputǁ_open__mutmut_20': xǁPlayerOutputǁ_open__mutmut_20, 
        'xǁPlayerOutputǁ_open__mutmut_21': xǁPlayerOutputǁ_open__mutmut_21, 
        'xǁPlayerOutputǁ_open__mutmut_22': xǁPlayerOutputǁ_open__mutmut_22, 
        'xǁPlayerOutputǁ_open__mutmut_23': xǁPlayerOutputǁ_open__mutmut_23, 
        'xǁPlayerOutputǁ_open__mutmut_24': xǁPlayerOutputǁ_open__mutmut_24, 
        'xǁPlayerOutputǁ_open__mutmut_25': xǁPlayerOutputǁ_open__mutmut_25, 
        'xǁPlayerOutputǁ_open__mutmut_26': xǁPlayerOutputǁ_open__mutmut_26, 
        'xǁPlayerOutputǁ_open__mutmut_27': xǁPlayerOutputǁ_open__mutmut_27, 
        'xǁPlayerOutputǁ_open__mutmut_28': xǁPlayerOutputǁ_open__mutmut_28, 
        'xǁPlayerOutputǁ_open__mutmut_29': xǁPlayerOutputǁ_open__mutmut_29, 
        'xǁPlayerOutputǁ_open__mutmut_30': xǁPlayerOutputǁ_open__mutmut_30, 
        'xǁPlayerOutputǁ_open__mutmut_31': xǁPlayerOutputǁ_open__mutmut_31, 
        'xǁPlayerOutputǁ_open__mutmut_32': xǁPlayerOutputǁ_open__mutmut_32, 
        'xǁPlayerOutputǁ_open__mutmut_33': xǁPlayerOutputǁ_open__mutmut_33, 
        'xǁPlayerOutputǁ_open__mutmut_34': xǁPlayerOutputǁ_open__mutmut_34, 
        'xǁPlayerOutputǁ_open__mutmut_35': xǁPlayerOutputǁ_open__mutmut_35, 
        'xǁPlayerOutputǁ_open__mutmut_36': xǁPlayerOutputǁ_open__mutmut_36, 
        'xǁPlayerOutputǁ_open__mutmut_37': xǁPlayerOutputǁ_open__mutmut_37, 
        'xǁPlayerOutputǁ_open__mutmut_38': xǁPlayerOutputǁ_open__mutmut_38, 
        'xǁPlayerOutputǁ_open__mutmut_39': xǁPlayerOutputǁ_open__mutmut_39, 
        'xǁPlayerOutputǁ_open__mutmut_40': xǁPlayerOutputǁ_open__mutmut_40, 
        'xǁPlayerOutputǁ_open__mutmut_41': xǁPlayerOutputǁ_open__mutmut_41, 
        'xǁPlayerOutputǁ_open__mutmut_42': xǁPlayerOutputǁ_open__mutmut_42, 
        'xǁPlayerOutputǁ_open__mutmut_43': xǁPlayerOutputǁ_open__mutmut_43, 
        'xǁPlayerOutputǁ_open__mutmut_44': xǁPlayerOutputǁ_open__mutmut_44, 
        'xǁPlayerOutputǁ_open__mutmut_45': xǁPlayerOutputǁ_open__mutmut_45, 
        'xǁPlayerOutputǁ_open__mutmut_46': xǁPlayerOutputǁ_open__mutmut_46, 
        'xǁPlayerOutputǁ_open__mutmut_47': xǁPlayerOutputǁ_open__mutmut_47, 
        'xǁPlayerOutputǁ_open__mutmut_48': xǁPlayerOutputǁ_open__mutmut_48
    }
    
    def _open(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ_open__mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ_open__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _open.__signature__ = _mutmut_signature(xǁPlayerOutputǁ_open__mutmut_orig)
    xǁPlayerOutputǁ_open__mutmut_orig.__name__ = 'xǁPlayerOutputǁ_open'

    def xǁPlayerOutputǁ_open_call__mutmut_orig(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_1(self, args: list[str]):
        log.debug(None)

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_2(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else 'XXXX'}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_3(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = None
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_4(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(None)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_5(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(None)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_6(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            None,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_7(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=None,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_8(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=None,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_9(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            stderr=None,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_10(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_11(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            stdout=self.stdout,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_12(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stderr=self.stderr,
        )

    def xǁPlayerOutputǁ_open_call__mutmut_13(self, args: list[str]):
        log.debug(f"Calling: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        subprocess.call(
            args,
            env=environ,
            stdout=self.stdout,
            )
    
    xǁPlayerOutputǁ_open_call__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ_open_call__mutmut_1': xǁPlayerOutputǁ_open_call__mutmut_1, 
        'xǁPlayerOutputǁ_open_call__mutmut_2': xǁPlayerOutputǁ_open_call__mutmut_2, 
        'xǁPlayerOutputǁ_open_call__mutmut_3': xǁPlayerOutputǁ_open_call__mutmut_3, 
        'xǁPlayerOutputǁ_open_call__mutmut_4': xǁPlayerOutputǁ_open_call__mutmut_4, 
        'xǁPlayerOutputǁ_open_call__mutmut_5': xǁPlayerOutputǁ_open_call__mutmut_5, 
        'xǁPlayerOutputǁ_open_call__mutmut_6': xǁPlayerOutputǁ_open_call__mutmut_6, 
        'xǁPlayerOutputǁ_open_call__mutmut_7': xǁPlayerOutputǁ_open_call__mutmut_7, 
        'xǁPlayerOutputǁ_open_call__mutmut_8': xǁPlayerOutputǁ_open_call__mutmut_8, 
        'xǁPlayerOutputǁ_open_call__mutmut_9': xǁPlayerOutputǁ_open_call__mutmut_9, 
        'xǁPlayerOutputǁ_open_call__mutmut_10': xǁPlayerOutputǁ_open_call__mutmut_10, 
        'xǁPlayerOutputǁ_open_call__mutmut_11': xǁPlayerOutputǁ_open_call__mutmut_11, 
        'xǁPlayerOutputǁ_open_call__mutmut_12': xǁPlayerOutputǁ_open_call__mutmut_12, 
        'xǁPlayerOutputǁ_open_call__mutmut_13': xǁPlayerOutputǁ_open_call__mutmut_13
    }
    
    def _open_call(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ_open_call__mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ_open_call__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _open_call.__signature__ = _mutmut_signature(xǁPlayerOutputǁ_open_call__mutmut_orig)
    xǁPlayerOutputǁ_open_call__mutmut_orig.__name__ = 'xǁPlayerOutputǁ_open_call'

    def xǁPlayerOutputǁ_open_subprocess__mutmut_orig(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_1(self, args: list[str]):
        log.debug(None)

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_2(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else 'XXXX'}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_3(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = None
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_4(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(None)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_5(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(None)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_6(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = None
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_7(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            None,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_8(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=None,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_9(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=None,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_10(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=None,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_11(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=None,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_12(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=None,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_13(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_14(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_15(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_16(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_17(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_18(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_19(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=1,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_20(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if self.running:
            raise OSError("Process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_21(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError(None)

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_22(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("XXProcess exited prematurelyXX")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_23(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("process exited prematurely")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()

    def xǁPlayerOutputǁ_open_subprocess__mutmut_24(self, args: list[str]):
        log.debug(f"Opening subprocess: {args!r}{f', env: {self.env!r}' if self.env else ''}")

        environ = dict(os.environ)
        environ.update(self.env)

        # Force bufsize=0 on all Python versions to avoid writing the
        # unflushed buffer when closing a broken input pipe
        self.player = subprocess.Popen(
            args,
            bufsize=0,
            env=environ,
            stdin=self.stdin,
            stdout=self.stdout,
            stderr=self.stderr,
        )
        # Wait 0.5 seconds to see if program exited prematurely
        if not self.running:
            raise OSError("PROCESS EXITED PREMATURELY")

        if self.namedpipe:
            self.namedpipe.open()
        elif self.http:
            self.http.accept_connection()
            self.http.open()
    
    xǁPlayerOutputǁ_open_subprocess__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ_open_subprocess__mutmut_1': xǁPlayerOutputǁ_open_subprocess__mutmut_1, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_2': xǁPlayerOutputǁ_open_subprocess__mutmut_2, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_3': xǁPlayerOutputǁ_open_subprocess__mutmut_3, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_4': xǁPlayerOutputǁ_open_subprocess__mutmut_4, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_5': xǁPlayerOutputǁ_open_subprocess__mutmut_5, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_6': xǁPlayerOutputǁ_open_subprocess__mutmut_6, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_7': xǁPlayerOutputǁ_open_subprocess__mutmut_7, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_8': xǁPlayerOutputǁ_open_subprocess__mutmut_8, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_9': xǁPlayerOutputǁ_open_subprocess__mutmut_9, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_10': xǁPlayerOutputǁ_open_subprocess__mutmut_10, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_11': xǁPlayerOutputǁ_open_subprocess__mutmut_11, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_12': xǁPlayerOutputǁ_open_subprocess__mutmut_12, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_13': xǁPlayerOutputǁ_open_subprocess__mutmut_13, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_14': xǁPlayerOutputǁ_open_subprocess__mutmut_14, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_15': xǁPlayerOutputǁ_open_subprocess__mutmut_15, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_16': xǁPlayerOutputǁ_open_subprocess__mutmut_16, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_17': xǁPlayerOutputǁ_open_subprocess__mutmut_17, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_18': xǁPlayerOutputǁ_open_subprocess__mutmut_18, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_19': xǁPlayerOutputǁ_open_subprocess__mutmut_19, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_20': xǁPlayerOutputǁ_open_subprocess__mutmut_20, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_21': xǁPlayerOutputǁ_open_subprocess__mutmut_21, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_22': xǁPlayerOutputǁ_open_subprocess__mutmut_22, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_23': xǁPlayerOutputǁ_open_subprocess__mutmut_23, 
        'xǁPlayerOutputǁ_open_subprocess__mutmut_24': xǁPlayerOutputǁ_open_subprocess__mutmut_24
    }
    
    def _open_subprocess(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ_open_subprocess__mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ_open_subprocess__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _open_subprocess.__signature__ = _mutmut_signature(xǁPlayerOutputǁ_open_subprocess__mutmut_orig)
    xǁPlayerOutputǁ_open_subprocess__mutmut_orig.__name__ = 'xǁPlayerOutputǁ_open_subprocess'

    def xǁPlayerOutputǁ_close__mutmut_orig(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_1(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_2(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(None):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_3(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_4(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = None
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_5(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 1.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_6(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is not None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_7(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None or t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_8(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t <= timeout:
                        sleep(0.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_9(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(None)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_10(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(1.5)
                        t += 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_11(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t = 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_12(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t -= 0.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_13(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 1.5

                    if not self.player.returncode:
                        self.player.kill()
        self.player.wait()

    def xǁPlayerOutputǁ_close__mutmut_14(self):
        # Close input to the player first to signal the end of the
        # stream and allow the player to terminate of its own accord
        if self.namedpipe:
            self.namedpipe.close()
        elif self.http:
            self.http.shutdown()
        elif not self.filename:
            self.player.stdin.close()

        if self.record:
            self.record.close()

        if self.kill:
            with suppress(Exception):
                self.player.terminate()
                if not is_win32:
                    t, timeout = 0.0, self.PLAYER_TERMINATE_TIMEOUT
                    while self.player.poll() is None and t < timeout:
                        sleep(0.5)
                        t += 0.5

                    if self.player.returncode:
                        self.player.kill()
        self.player.wait()
    
    xǁPlayerOutputǁ_close__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ_close__mutmut_1': xǁPlayerOutputǁ_close__mutmut_1, 
        'xǁPlayerOutputǁ_close__mutmut_2': xǁPlayerOutputǁ_close__mutmut_2, 
        'xǁPlayerOutputǁ_close__mutmut_3': xǁPlayerOutputǁ_close__mutmut_3, 
        'xǁPlayerOutputǁ_close__mutmut_4': xǁPlayerOutputǁ_close__mutmut_4, 
        'xǁPlayerOutputǁ_close__mutmut_5': xǁPlayerOutputǁ_close__mutmut_5, 
        'xǁPlayerOutputǁ_close__mutmut_6': xǁPlayerOutputǁ_close__mutmut_6, 
        'xǁPlayerOutputǁ_close__mutmut_7': xǁPlayerOutputǁ_close__mutmut_7, 
        'xǁPlayerOutputǁ_close__mutmut_8': xǁPlayerOutputǁ_close__mutmut_8, 
        'xǁPlayerOutputǁ_close__mutmut_9': xǁPlayerOutputǁ_close__mutmut_9, 
        'xǁPlayerOutputǁ_close__mutmut_10': xǁPlayerOutputǁ_close__mutmut_10, 
        'xǁPlayerOutputǁ_close__mutmut_11': xǁPlayerOutputǁ_close__mutmut_11, 
        'xǁPlayerOutputǁ_close__mutmut_12': xǁPlayerOutputǁ_close__mutmut_12, 
        'xǁPlayerOutputǁ_close__mutmut_13': xǁPlayerOutputǁ_close__mutmut_13, 
        'xǁPlayerOutputǁ_close__mutmut_14': xǁPlayerOutputǁ_close__mutmut_14
    }
    
    def _close(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ_close__mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ_close__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _close.__signature__ = _mutmut_signature(xǁPlayerOutputǁ_close__mutmut_orig)
    xǁPlayerOutputǁ_close__mutmut_orig.__name__ = 'xǁPlayerOutputǁ_close'

    def xǁPlayerOutputǁ_write__mutmut_orig(self, data):
        if self.record:
            self.record.write(data)

        if self.namedpipe:
            self.namedpipe.write(data)
        elif self.http:
            self.http.write(data)
        else:
            self.player.stdin.write(data)

    def xǁPlayerOutputǁ_write__mutmut_1(self, data):
        if self.record:
            self.record.write(None)

        if self.namedpipe:
            self.namedpipe.write(data)
        elif self.http:
            self.http.write(data)
        else:
            self.player.stdin.write(data)

    def xǁPlayerOutputǁ_write__mutmut_2(self, data):
        if self.record:
            self.record.write(data)

        if self.namedpipe:
            self.namedpipe.write(None)
        elif self.http:
            self.http.write(data)
        else:
            self.player.stdin.write(data)

    def xǁPlayerOutputǁ_write__mutmut_3(self, data):
        if self.record:
            self.record.write(data)

        if self.namedpipe:
            self.namedpipe.write(data)
        elif self.http:
            self.http.write(None)
        else:
            self.player.stdin.write(data)

    def xǁPlayerOutputǁ_write__mutmut_4(self, data):
        if self.record:
            self.record.write(data)

        if self.namedpipe:
            self.namedpipe.write(data)
        elif self.http:
            self.http.write(data)
        else:
            self.player.stdin.write(None)
    
    xǁPlayerOutputǁ_write__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁPlayerOutputǁ_write__mutmut_1': xǁPlayerOutputǁ_write__mutmut_1, 
        'xǁPlayerOutputǁ_write__mutmut_2': xǁPlayerOutputǁ_write__mutmut_2, 
        'xǁPlayerOutputǁ_write__mutmut_3': xǁPlayerOutputǁ_write__mutmut_3, 
        'xǁPlayerOutputǁ_write__mutmut_4': xǁPlayerOutputǁ_write__mutmut_4
    }
    
    def _write(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁPlayerOutputǁ_write__mutmut_orig"), object.__getattribute__(self, "xǁPlayerOutputǁ_write__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _write.__signature__ = _mutmut_signature(xǁPlayerOutputǁ_write__mutmut_orig)
    xǁPlayerOutputǁ_write__mutmut_orig.__name__ = 'xǁPlayerOutputǁ_write'

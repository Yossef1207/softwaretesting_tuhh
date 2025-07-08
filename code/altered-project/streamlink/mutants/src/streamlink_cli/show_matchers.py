from __future__ import annotations

import re
from textwrap import dedent, indent

from streamlink.plugin.plugin import HIGH_PRIORITY, LOW_PRIORITY, NO_PRIORITY, NORMAL_PRIORITY, Matchers
from streamlink.session import Streamlink
from streamlink_cli.console import ConsoleOutput
from streamlink_cli.exceptions import StreamlinkCLIError


PRIORITY_NAMES = {
    NO_PRIORITY: "NONE",
    LOW_PRIORITY: "LOW",
    HIGH_PRIORITY: "HIGH",
}

# noinspection PyTypeChecker
PATTERN_FLAG_NAMES: dict[int, str] = {
    flag.value: flag.name
    for flag in (re.IGNORECASE, re.VERBOSE)
    if flag.name
}  # fmt: skip
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


def x_show_matchers__mutmut_orig(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_1(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = None

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_2(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(None)

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_3(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_4(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError(None, code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_5(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=None)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_6(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError(code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_7(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", )

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_8(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("XXPlugin not foundXX", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_9(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_10(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("PLUGIN NOT FOUND", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_11(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=2)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_12(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = None

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_13(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(None)
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_14(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(None))
    else:
        console.msg(show_matchers_text(matchers))


def x_show_matchers__mutmut_15(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(None)


def x_show_matchers__mutmut_16(session: Streamlink, console: ConsoleOutput, pluginname: str):
    available = dict(session.plugins.iter_matchers())

    if pluginname not in available:
        raise StreamlinkCLIError("Plugin not found", code=1)

    matchers = available[pluginname]

    if console.json:
        console.msg_json(show_matchers_json(matchers))
    else:
        console.msg(show_matchers_text(None))

x_show_matchers__mutmut_mutants : ClassVar[MutantDict] = {
'x_show_matchers__mutmut_1': x_show_matchers__mutmut_1, 
    'x_show_matchers__mutmut_2': x_show_matchers__mutmut_2, 
    'x_show_matchers__mutmut_3': x_show_matchers__mutmut_3, 
    'x_show_matchers__mutmut_4': x_show_matchers__mutmut_4, 
    'x_show_matchers__mutmut_5': x_show_matchers__mutmut_5, 
    'x_show_matchers__mutmut_6': x_show_matchers__mutmut_6, 
    'x_show_matchers__mutmut_7': x_show_matchers__mutmut_7, 
    'x_show_matchers__mutmut_8': x_show_matchers__mutmut_8, 
    'x_show_matchers__mutmut_9': x_show_matchers__mutmut_9, 
    'x_show_matchers__mutmut_10': x_show_matchers__mutmut_10, 
    'x_show_matchers__mutmut_11': x_show_matchers__mutmut_11, 
    'x_show_matchers__mutmut_12': x_show_matchers__mutmut_12, 
    'x_show_matchers__mutmut_13': x_show_matchers__mutmut_13, 
    'x_show_matchers__mutmut_14': x_show_matchers__mutmut_14, 
    'x_show_matchers__mutmut_15': x_show_matchers__mutmut_15, 
    'x_show_matchers__mutmut_16': x_show_matchers__mutmut_16
}

def show_matchers(*args, **kwargs):
    result = _mutmut_trampoline(x_show_matchers__mutmut_orig, x_show_matchers__mutmut_mutants, args, kwargs)
    return result 

show_matchers.__signature__ = _mutmut_signature(x_show_matchers__mutmut_orig)
x_show_matchers__mutmut_orig.__name__ = 'x_show_matchers'


def x_show_matchers_text__mutmut_orig(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_1(matchers: Matchers) -> str:
    output = None
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_2(matchers: Matchers) -> str:
    output = []
    indentation = None
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_3(matchers: Matchers) -> str:
    output = []
    indentation = "XX  XX"
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_4(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers and []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_5(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = None
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_6(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = None
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_7(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags | val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_8(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(None)
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_9(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority == NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_10(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(None)
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_11(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(None, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_12(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, None)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_13(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_14(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, )}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_15(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(None)
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_16(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(None)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_17(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {'XX & XX'.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_18(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags | re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_19(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(None)
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_20(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(None, indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_21(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), None)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_22(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_23(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), )}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_24(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(None).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_25(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(None)
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_26(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = None
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_27(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent(None, indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_28(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), None)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_29(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent(indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_30(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), )
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_31(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(None), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_32(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("XX\nXX".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_33(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\N".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_34(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(None)

    return "\n".join(output)


def x_show_matchers_text__mutmut_35(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[3:]}")

    return "\n".join(output)


def x_show_matchers_text__mutmut_36(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\n".join(None)


def x_show_matchers_text__mutmut_37(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "XX\nXX".join(output)


def x_show_matchers_text__mutmut_38(matchers: Matchers) -> str:
    output = []
    indentation = "  "
    for matcher in matchers or []:
        data = []
        flags = [name for val, name in PATTERN_FLAG_NAMES.items() if matcher.pattern.flags & val]
        if matcher.name:
            data.append(f"name: {matcher.name}")
        if matcher.priority != NORMAL_PRIORITY:
            data.append(f"priority: {PRIORITY_NAMES.get(matcher.priority, matcher.priority)}")
        if flags:
            data.append(f"flags: {' & '.join(flags)}")
        if matcher.pattern.flags & re.VERBOSE:
            data.append(f"pattern:\n{indent(dedent(matcher.pattern.pattern).strip(), indentation)}")
        else:
            data.append(f"pattern: {matcher.pattern.pattern}")
        item = indent("\n".join(data), indentation)
        output.append(f"- {item[2:]}")

    return "\N".join(output)

x_show_matchers_text__mutmut_mutants : ClassVar[MutantDict] = {
'x_show_matchers_text__mutmut_1': x_show_matchers_text__mutmut_1, 
    'x_show_matchers_text__mutmut_2': x_show_matchers_text__mutmut_2, 
    'x_show_matchers_text__mutmut_3': x_show_matchers_text__mutmut_3, 
    'x_show_matchers_text__mutmut_4': x_show_matchers_text__mutmut_4, 
    'x_show_matchers_text__mutmut_5': x_show_matchers_text__mutmut_5, 
    'x_show_matchers_text__mutmut_6': x_show_matchers_text__mutmut_6, 
    'x_show_matchers_text__mutmut_7': x_show_matchers_text__mutmut_7, 
    'x_show_matchers_text__mutmut_8': x_show_matchers_text__mutmut_8, 
    'x_show_matchers_text__mutmut_9': x_show_matchers_text__mutmut_9, 
    'x_show_matchers_text__mutmut_10': x_show_matchers_text__mutmut_10, 
    'x_show_matchers_text__mutmut_11': x_show_matchers_text__mutmut_11, 
    'x_show_matchers_text__mutmut_12': x_show_matchers_text__mutmut_12, 
    'x_show_matchers_text__mutmut_13': x_show_matchers_text__mutmut_13, 
    'x_show_matchers_text__mutmut_14': x_show_matchers_text__mutmut_14, 
    'x_show_matchers_text__mutmut_15': x_show_matchers_text__mutmut_15, 
    'x_show_matchers_text__mutmut_16': x_show_matchers_text__mutmut_16, 
    'x_show_matchers_text__mutmut_17': x_show_matchers_text__mutmut_17, 
    'x_show_matchers_text__mutmut_18': x_show_matchers_text__mutmut_18, 
    'x_show_matchers_text__mutmut_19': x_show_matchers_text__mutmut_19, 
    'x_show_matchers_text__mutmut_20': x_show_matchers_text__mutmut_20, 
    'x_show_matchers_text__mutmut_21': x_show_matchers_text__mutmut_21, 
    'x_show_matchers_text__mutmut_22': x_show_matchers_text__mutmut_22, 
    'x_show_matchers_text__mutmut_23': x_show_matchers_text__mutmut_23, 
    'x_show_matchers_text__mutmut_24': x_show_matchers_text__mutmut_24, 
    'x_show_matchers_text__mutmut_25': x_show_matchers_text__mutmut_25, 
    'x_show_matchers_text__mutmut_26': x_show_matchers_text__mutmut_26, 
    'x_show_matchers_text__mutmut_27': x_show_matchers_text__mutmut_27, 
    'x_show_matchers_text__mutmut_28': x_show_matchers_text__mutmut_28, 
    'x_show_matchers_text__mutmut_29': x_show_matchers_text__mutmut_29, 
    'x_show_matchers_text__mutmut_30': x_show_matchers_text__mutmut_30, 
    'x_show_matchers_text__mutmut_31': x_show_matchers_text__mutmut_31, 
    'x_show_matchers_text__mutmut_32': x_show_matchers_text__mutmut_32, 
    'x_show_matchers_text__mutmut_33': x_show_matchers_text__mutmut_33, 
    'x_show_matchers_text__mutmut_34': x_show_matchers_text__mutmut_34, 
    'x_show_matchers_text__mutmut_35': x_show_matchers_text__mutmut_35, 
    'x_show_matchers_text__mutmut_36': x_show_matchers_text__mutmut_36, 
    'x_show_matchers_text__mutmut_37': x_show_matchers_text__mutmut_37, 
    'x_show_matchers_text__mutmut_38': x_show_matchers_text__mutmut_38
}

def show_matchers_text(*args, **kwargs):
    result = _mutmut_trampoline(x_show_matchers_text__mutmut_orig, x_show_matchers_text__mutmut_mutants, args, kwargs)
    return result 

show_matchers_text.__signature__ = _mutmut_signature(x_show_matchers_text__mutmut_orig)
x_show_matchers_text__mutmut_orig.__name__ = 'x_show_matchers_text'


def x_show_matchers_json__mutmut_orig(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_1(matchers: Matchers) -> list[dict]:
    return [
        {
            "XXnameXX": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_2(matchers: Matchers) -> list[dict]:
    return [
        {
            "NAME": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_3(matchers: Matchers) -> list[dict]:
    return [
        {
            "Name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_4(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "XXpriorityXX": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_5(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "PRIORITY": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_6(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "Priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_7(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "XXflagsXX": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_8(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "FLAGS": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_9(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "Flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_10(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags | ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_11(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_12(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "XXpatternXX": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_13(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "PATTERN": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_14(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "Pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_15(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(None).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_16(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags | re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers or []
    ]  # fmt: skip


def x_show_matchers_json__mutmut_17(matchers: Matchers) -> list[dict]:
    return [
        {
            "name": matcher.name,
            "priority": matcher.priority,
            "flags": matcher.pattern.flags & ~re.UNICODE,
            "pattern": (
                dedent(matcher.pattern.pattern).strip()
                if matcher.pattern.flags & re.VERBOSE
                else matcher.pattern.pattern
            ),
        }
        for matcher in matchers and []
    ]  # fmt: skip

x_show_matchers_json__mutmut_mutants : ClassVar[MutantDict] = {
'x_show_matchers_json__mutmut_1': x_show_matchers_json__mutmut_1, 
    'x_show_matchers_json__mutmut_2': x_show_matchers_json__mutmut_2, 
    'x_show_matchers_json__mutmut_3': x_show_matchers_json__mutmut_3, 
    'x_show_matchers_json__mutmut_4': x_show_matchers_json__mutmut_4, 
    'x_show_matchers_json__mutmut_5': x_show_matchers_json__mutmut_5, 
    'x_show_matchers_json__mutmut_6': x_show_matchers_json__mutmut_6, 
    'x_show_matchers_json__mutmut_7': x_show_matchers_json__mutmut_7, 
    'x_show_matchers_json__mutmut_8': x_show_matchers_json__mutmut_8, 
    'x_show_matchers_json__mutmut_9': x_show_matchers_json__mutmut_9, 
    'x_show_matchers_json__mutmut_10': x_show_matchers_json__mutmut_10, 
    'x_show_matchers_json__mutmut_11': x_show_matchers_json__mutmut_11, 
    'x_show_matchers_json__mutmut_12': x_show_matchers_json__mutmut_12, 
    'x_show_matchers_json__mutmut_13': x_show_matchers_json__mutmut_13, 
    'x_show_matchers_json__mutmut_14': x_show_matchers_json__mutmut_14, 
    'x_show_matchers_json__mutmut_15': x_show_matchers_json__mutmut_15, 
    'x_show_matchers_json__mutmut_16': x_show_matchers_json__mutmut_16, 
    'x_show_matchers_json__mutmut_17': x_show_matchers_json__mutmut_17
}

def show_matchers_json(*args, **kwargs):
    result = _mutmut_trampoline(x_show_matchers_json__mutmut_orig, x_show_matchers_json__mutmut_mutants, args, kwargs)
    return result 

show_matchers_json.__signature__ = _mutmut_signature(x_show_matchers_json__mutmut_orig)
x_show_matchers_json__mutmut_orig.__name__ = 'x_show_matchers_json'

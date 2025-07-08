from shutil import get_terminal_size
from typing import Iterable

from streamlink.compat import is_win32


# widths generated from
# https://www.unicode.org/Public/4.0-Update/EastAsianWidth-4.0.0.txt
# See https://github.com/streamlink/streamlink/pull/2032
WIDTHS: Iterable[tuple[int, int]] = (
    (13, 1),
    (15, 0),
    (126, 1),
    (159, 0),
    (687, 1),
    (710, 0),
    (711, 1),
    (727, 0),
    (733, 1),
    (879, 0),
    (1154, 1),
    (1161, 0),
    (4347, 1),
    (4447, 2),
    (7467, 1),
    (7521, 0),
    (8369, 1),
    (8426, 0),
    (9000, 1),
    (9002, 2),
    (11021, 1),
    (12350, 2),
    (12351, 1),
    (12438, 2),
    (12442, 0),
    (19893, 2),
    (19967, 1),
    (55203, 2),
    (63743, 1),
    (64106, 2),
    (65039, 1),
    (65059, 0),
    (65131, 2),
    (65279, 1),
    (65376, 2),
    (65500, 1),
    (65510, 2),
    (120831, 1),
    (262141, 2),
    (1114109, 1),
)

# On Windows, we need one less space, or we overflow the line for some reason.
GAP = 1 if is_win32 else 0
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


def x_term_width__mutmut_orig():
    return get_terminal_size().columns - GAP


def x_term_width__mutmut_1():
    return get_terminal_size().columns + GAP

x_term_width__mutmut_mutants : ClassVar[MutantDict] = {
'x_term_width__mutmut_1': x_term_width__mutmut_1
}

def term_width(*args, **kwargs):
    result = _mutmut_trampoline(x_term_width__mutmut_orig, x_term_width__mutmut_mutants, args, kwargs)
    return result 

term_width.__signature__ = _mutmut_signature(x_term_width__mutmut_orig)
x_term_width__mutmut_orig.__name__ = 'x_term_width'


def x__get_width__mutmut_orig(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next((width for unicode, width in WIDTHS if ordinal <= unicode), 1)


def x__get_width__mutmut_1(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next(None, 1)


def x__get_width__mutmut_2(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next((width for unicode, width in WIDTHS if ordinal <= unicode), None)


def x__get_width__mutmut_3(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next(1)


def x__get_width__mutmut_4(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next((width for unicode, width in WIDTHS if ordinal <= unicode), )


def x__get_width__mutmut_5(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next((width for unicode, width in WIDTHS if ordinal < unicode), 1)


def x__get_width__mutmut_6(ordinal: int) -> int:
    """Return the width of a specific unicode character when it would be displayed."""
    return next((width for unicode, width in WIDTHS if ordinal <= unicode), 2)

x__get_width__mutmut_mutants : ClassVar[MutantDict] = {
'x__get_width__mutmut_1': x__get_width__mutmut_1, 
    'x__get_width__mutmut_2': x__get_width__mutmut_2, 
    'x__get_width__mutmut_3': x__get_width__mutmut_3, 
    'x__get_width__mutmut_4': x__get_width__mutmut_4, 
    'x__get_width__mutmut_5': x__get_width__mutmut_5, 
    'x__get_width__mutmut_6': x__get_width__mutmut_6
}

def _get_width(*args, **kwargs):
    result = _mutmut_trampoline(x__get_width__mutmut_orig, x__get_width__mutmut_mutants, args, kwargs)
    return result 

_get_width.__signature__ = _mutmut_signature(x__get_width__mutmut_orig)
x__get_width__mutmut_orig.__name__ = 'x__get_width'


def x_text_width__mutmut_orig(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, map(ord, value)))


def x_text_width__mutmut_1(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(None)


def x_text_width__mutmut_2(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(None, map(ord, value)))


def x_text_width__mutmut_3(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, None))


def x_text_width__mutmut_4(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(map(ord, value)))


def x_text_width__mutmut_5(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, ))


def x_text_width__mutmut_6(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, map(None, value)))


def x_text_width__mutmut_7(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, map(ord, None)))


def x_text_width__mutmut_8(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, map(value)))


def x_text_width__mutmut_9(value: str):
    """Return the overall width of a string when it would be displayed."""
    return sum(map(_get_width, map(ord, )))

x_text_width__mutmut_mutants : ClassVar[MutantDict] = {
'x_text_width__mutmut_1': x_text_width__mutmut_1, 
    'x_text_width__mutmut_2': x_text_width__mutmut_2, 
    'x_text_width__mutmut_3': x_text_width__mutmut_3, 
    'x_text_width__mutmut_4': x_text_width__mutmut_4, 
    'x_text_width__mutmut_5': x_text_width__mutmut_5, 
    'x_text_width__mutmut_6': x_text_width__mutmut_6, 
    'x_text_width__mutmut_7': x_text_width__mutmut_7, 
    'x_text_width__mutmut_8': x_text_width__mutmut_8, 
    'x_text_width__mutmut_9': x_text_width__mutmut_9
}

def text_width(*args, **kwargs):
    result = _mutmut_trampoline(x_text_width__mutmut_orig, x_text_width__mutmut_mutants, args, kwargs)
    return result 

text_width.__signature__ = _mutmut_signature(x_text_width__mutmut_orig)
x_text_width__mutmut_orig.__name__ = 'x_text_width'


def x_cut_text__mutmut_orig(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(len(value)):  # pragma: no branch
        current = value[i:]
        if text_width(current) <= max_width:
            break

    return current


def x_cut_text__mutmut_1(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = None
    for i in range(len(value)):  # pragma: no branch
        current = value[i:]
        if text_width(current) <= max_width:
            break

    return current


def x_cut_text__mutmut_2(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(None):  # pragma: no branch
        current = value[i:]
        if text_width(current) <= max_width:
            break

    return current


def x_cut_text__mutmut_3(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(len(value)):  # pragma: no branch
        current = None
        if text_width(current) <= max_width:
            break

    return current


def x_cut_text__mutmut_4(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(len(value)):  # pragma: no branch
        current = value[i:]
        if text_width(None) <= max_width:
            break

    return current


def x_cut_text__mutmut_5(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(len(value)):  # pragma: no branch
        current = value[i:]
        if text_width(current) < max_width:
            break

    return current


def x_cut_text__mutmut_6(value: str, max_width: int) -> str:
    """Cut off the beginning of a string until its display width fits into the output size."""
    current = value
    for i in range(len(value)):  # pragma: no branch
        current = value[i:]
        if text_width(current) <= max_width:
            return

    return current

x_cut_text__mutmut_mutants : ClassVar[MutantDict] = {
'x_cut_text__mutmut_1': x_cut_text__mutmut_1, 
    'x_cut_text__mutmut_2': x_cut_text__mutmut_2, 
    'x_cut_text__mutmut_3': x_cut_text__mutmut_3, 
    'x_cut_text__mutmut_4': x_cut_text__mutmut_4, 
    'x_cut_text__mutmut_5': x_cut_text__mutmut_5, 
    'x_cut_text__mutmut_6': x_cut_text__mutmut_6
}

def cut_text(*args, **kwargs):
    result = _mutmut_trampoline(x_cut_text__mutmut_orig, x_cut_text__mutmut_mutants, args, kwargs)
    return result 

cut_text.__signature__ = _mutmut_signature(x_cut_text__mutmut_orig)
x_cut_text__mutmut_orig.__name__ = 'x_cut_text'

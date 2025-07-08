from __future__ import annotations

import operator
from collections.abc import Callable, Container, Mapping
from typing import Any, Literal
from urllib.parse import urlparse

from lxml.etree import XPathError, iselement

from streamlink.utils.parse import (
    parse_html as _parse_html,
    parse_json as _parse_json,
    parse_qsd as _parse_qsd,
    parse_xml as _parse_xml,
)
from streamlink.validate._exception import ValidationError
from streamlink.validate._schemas import AllSchema, AnySchema, TransformSchema
from streamlink.validate._validate import validate


# String related validators

_validator_length_ops: Mapping[str, tuple[Callable, str]] = {
    "lt": (operator.lt, "Length must be <{number}, but value is {value}"),
    "le": (operator.le, "Length must be <={number}, but value is {value}"),
    "eq": (operator.eq, "Length must be =={number}, but value is {value}"),
    "ge": (operator.ge, "Length must be >={number}, but value is {value}"),
    "gt": (operator.gt, "Length must be >{number}, but value is {value}"),
}
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


def x_validator_length__mutmut_orig(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_1(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "XXgeXX",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_2(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "GE",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_3(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "Ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_4(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = None
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_5(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(None, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_6(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, None)
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_7(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get("ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_8(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, )
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_9(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "XXgeXX")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_10(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "GE")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_11(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "Ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_12(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_13(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(None, number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_14(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), None):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_15(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_16(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), ):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_17(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                None,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_18(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=None,
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_19(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=None,
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_20(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema=None,
            )

        return True

    return length


def x_validator_length__mutmut_21(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_22(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_23(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_24(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                )

        return True

    return length


def x_validator_length__mutmut_25(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(None),
                value=len(value),
                schema="length",
            )

        return True

    return length


def x_validator_length__mutmut_26(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="XXlengthXX",
            )

        return True

    return length


def x_validator_length__mutmut_27(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="LENGTH",
            )

        return True

    return length


def x_validator_length__mutmut_28(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="Length",
            )

        return True

    return length


def x_validator_length__mutmut_29(
    number: int,
    op: Literal["lt", "le", "eq", "ge", "gt"] = "ge",
) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input has a certain length, by using :func:`len()`.
    Checks the minimum length by default (``op="ge"``).

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3),
        )
        assert schema.validate("abc") == "abc"
        assert schema.validate([1, 2, 3, 4]) == [1, 2, 3, 4]
        schema.validate("a")  # raises ValidationError
        schema.validate([1])  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.length(3, op="lt"),
        )
        assert schema.validate("ab") == "ab"
        schema.validate([1, 2, 3])  # raises ValidationError
    """

    def length(value):
        func, msg = _validator_length_ops.get(op, "ge")
        if not func(len(value), number):
            raise ValidationError(
                msg,
                number=repr(number),
                value=len(value),
                schema="length",
            )

        return False

    return length

x_validator_length__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_length__mutmut_1': x_validator_length__mutmut_1, 
    'x_validator_length__mutmut_2': x_validator_length__mutmut_2, 
    'x_validator_length__mutmut_3': x_validator_length__mutmut_3, 
    'x_validator_length__mutmut_4': x_validator_length__mutmut_4, 
    'x_validator_length__mutmut_5': x_validator_length__mutmut_5, 
    'x_validator_length__mutmut_6': x_validator_length__mutmut_6, 
    'x_validator_length__mutmut_7': x_validator_length__mutmut_7, 
    'x_validator_length__mutmut_8': x_validator_length__mutmut_8, 
    'x_validator_length__mutmut_9': x_validator_length__mutmut_9, 
    'x_validator_length__mutmut_10': x_validator_length__mutmut_10, 
    'x_validator_length__mutmut_11': x_validator_length__mutmut_11, 
    'x_validator_length__mutmut_12': x_validator_length__mutmut_12, 
    'x_validator_length__mutmut_13': x_validator_length__mutmut_13, 
    'x_validator_length__mutmut_14': x_validator_length__mutmut_14, 
    'x_validator_length__mutmut_15': x_validator_length__mutmut_15, 
    'x_validator_length__mutmut_16': x_validator_length__mutmut_16, 
    'x_validator_length__mutmut_17': x_validator_length__mutmut_17, 
    'x_validator_length__mutmut_18': x_validator_length__mutmut_18, 
    'x_validator_length__mutmut_19': x_validator_length__mutmut_19, 
    'x_validator_length__mutmut_20': x_validator_length__mutmut_20, 
    'x_validator_length__mutmut_21': x_validator_length__mutmut_21, 
    'x_validator_length__mutmut_22': x_validator_length__mutmut_22, 
    'x_validator_length__mutmut_23': x_validator_length__mutmut_23, 
    'x_validator_length__mutmut_24': x_validator_length__mutmut_24, 
    'x_validator_length__mutmut_25': x_validator_length__mutmut_25, 
    'x_validator_length__mutmut_26': x_validator_length__mutmut_26, 
    'x_validator_length__mutmut_27': x_validator_length__mutmut_27, 
    'x_validator_length__mutmut_28': x_validator_length__mutmut_28, 
    'x_validator_length__mutmut_29': x_validator_length__mutmut_29
}

def validator_length(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_length__mutmut_orig, x_validator_length__mutmut_mutants, args, kwargs)
    return result 

validator_length.__signature__ = _mutmut_signature(x_validator_length__mutmut_orig)
x_validator_length__mutmut_orig.__name__ = 'x_validator_length'


def x_validator_startswith__mutmut_orig(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_1(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(None, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_2(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, None)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_3(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_4(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, )
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_5(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_6(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(None):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_7(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                None,
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_8(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=None,
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_9(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=None,
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_10(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema=None,
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_11(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_12(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_13(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_14(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                )

        return True

    return starts_with


def x_validator_startswith__mutmut_15(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "XX{value} does not start with {string}XX",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_16(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{VALUE} DOES NOT START WITH {STRING}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_17(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(None),
                string=repr(string),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_18(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(None),
                schema="startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_19(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="XXstartswithXX",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_20(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="STARTSWITH",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_21(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="Startswith",
            )

        return True

    return starts_with


def x_validator_startswith__mutmut_22(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string starts with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.startswith("1"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't start with ``string``
    """

    def starts_with(value):
        validate(str, value)
        if not value.startswith(string):
            raise ValidationError(
                "{value} does not start with {string}",
                value=repr(value),
                string=repr(string),
                schema="startswith",
            )

        return False

    return starts_with

x_validator_startswith__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_startswith__mutmut_1': x_validator_startswith__mutmut_1, 
    'x_validator_startswith__mutmut_2': x_validator_startswith__mutmut_2, 
    'x_validator_startswith__mutmut_3': x_validator_startswith__mutmut_3, 
    'x_validator_startswith__mutmut_4': x_validator_startswith__mutmut_4, 
    'x_validator_startswith__mutmut_5': x_validator_startswith__mutmut_5, 
    'x_validator_startswith__mutmut_6': x_validator_startswith__mutmut_6, 
    'x_validator_startswith__mutmut_7': x_validator_startswith__mutmut_7, 
    'x_validator_startswith__mutmut_8': x_validator_startswith__mutmut_8, 
    'x_validator_startswith__mutmut_9': x_validator_startswith__mutmut_9, 
    'x_validator_startswith__mutmut_10': x_validator_startswith__mutmut_10, 
    'x_validator_startswith__mutmut_11': x_validator_startswith__mutmut_11, 
    'x_validator_startswith__mutmut_12': x_validator_startswith__mutmut_12, 
    'x_validator_startswith__mutmut_13': x_validator_startswith__mutmut_13, 
    'x_validator_startswith__mutmut_14': x_validator_startswith__mutmut_14, 
    'x_validator_startswith__mutmut_15': x_validator_startswith__mutmut_15, 
    'x_validator_startswith__mutmut_16': x_validator_startswith__mutmut_16, 
    'x_validator_startswith__mutmut_17': x_validator_startswith__mutmut_17, 
    'x_validator_startswith__mutmut_18': x_validator_startswith__mutmut_18, 
    'x_validator_startswith__mutmut_19': x_validator_startswith__mutmut_19, 
    'x_validator_startswith__mutmut_20': x_validator_startswith__mutmut_20, 
    'x_validator_startswith__mutmut_21': x_validator_startswith__mutmut_21, 
    'x_validator_startswith__mutmut_22': x_validator_startswith__mutmut_22
}

def validator_startswith(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_startswith__mutmut_orig, x_validator_startswith__mutmut_mutants, args, kwargs)
    return result 

validator_startswith.__signature__ = _mutmut_signature(x_validator_startswith__mutmut_orig)
x_validator_startswith__mutmut_orig.__name__ = 'x_validator_startswith'


def x_validator_endswith__mutmut_orig(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_1(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(None, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_2(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, None)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_3(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_4(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, )
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_5(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_6(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(None):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_7(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                None,
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_8(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=None,
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_9(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=None,
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_10(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema=None,
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_11(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_12(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_13(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_14(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                )

        return True

    return ends_with


def x_validator_endswith__mutmut_15(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "XX{value} does not end with {string}XX",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_16(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{VALUE} DOES NOT END WITH {STRING}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_17(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(None),
                string=repr(string),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_18(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(None),
                schema="endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_19(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="XXendswithXX",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_20(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="ENDSWITH",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_21(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="Endswith",
            )

        return True

    return ends_with


def x_validator_endswith__mutmut_22(string: str) -> Callable[[str], bool]:
    """
    Utility function for checking whether the input string ends with another string.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.endswith("3"),
        )
        assert schema.validate("123") == "123"
        schema.validate("321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`str`
    :raise ValidationError: If input doesn't end with ``string``
    """

    def ends_with(value):
        validate(str, value)
        if not value.endswith(string):
            raise ValidationError(
                "{value} does not end with {string}",
                value=repr(value),
                string=repr(string),
                schema="endswith",
            )

        return False

    return ends_with

x_validator_endswith__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_endswith__mutmut_1': x_validator_endswith__mutmut_1, 
    'x_validator_endswith__mutmut_2': x_validator_endswith__mutmut_2, 
    'x_validator_endswith__mutmut_3': x_validator_endswith__mutmut_3, 
    'x_validator_endswith__mutmut_4': x_validator_endswith__mutmut_4, 
    'x_validator_endswith__mutmut_5': x_validator_endswith__mutmut_5, 
    'x_validator_endswith__mutmut_6': x_validator_endswith__mutmut_6, 
    'x_validator_endswith__mutmut_7': x_validator_endswith__mutmut_7, 
    'x_validator_endswith__mutmut_8': x_validator_endswith__mutmut_8, 
    'x_validator_endswith__mutmut_9': x_validator_endswith__mutmut_9, 
    'x_validator_endswith__mutmut_10': x_validator_endswith__mutmut_10, 
    'x_validator_endswith__mutmut_11': x_validator_endswith__mutmut_11, 
    'x_validator_endswith__mutmut_12': x_validator_endswith__mutmut_12, 
    'x_validator_endswith__mutmut_13': x_validator_endswith__mutmut_13, 
    'x_validator_endswith__mutmut_14': x_validator_endswith__mutmut_14, 
    'x_validator_endswith__mutmut_15': x_validator_endswith__mutmut_15, 
    'x_validator_endswith__mutmut_16': x_validator_endswith__mutmut_16, 
    'x_validator_endswith__mutmut_17': x_validator_endswith__mutmut_17, 
    'x_validator_endswith__mutmut_18': x_validator_endswith__mutmut_18, 
    'x_validator_endswith__mutmut_19': x_validator_endswith__mutmut_19, 
    'x_validator_endswith__mutmut_20': x_validator_endswith__mutmut_20, 
    'x_validator_endswith__mutmut_21': x_validator_endswith__mutmut_21, 
    'x_validator_endswith__mutmut_22': x_validator_endswith__mutmut_22
}

def validator_endswith(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_endswith__mutmut_orig, x_validator_endswith__mutmut_mutants, args, kwargs)
    return result 

validator_endswith.__signature__ = _mutmut_signature(x_validator_endswith__mutmut_orig)
x_validator_endswith__mutmut_orig.__name__ = 'x_validator_endswith'


def x_validator_contains__mutmut_orig(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_1(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(None, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_2(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, None)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_3(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_4(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, )
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_5(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_6(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                None,
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_7(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=None,
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_8(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=None,
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_9(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema=None,
            )

        return True

    return contains_str


def x_validator_contains__mutmut_10(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_11(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_12(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_13(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                )

        return True

    return contains_str


def x_validator_contains__mutmut_14(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "XX{value} does not contain {obj}XX",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_15(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{VALUE} DOES NOT CONTAIN {OBJ}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_16(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(None),
                obj=repr(obj),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_17(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(None),
                schema="contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_18(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="XXcontainsXX",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_19(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="CONTAINS",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_20(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="Contains",
            )

        return True

    return contains_str


def x_validator_contains__mutmut_21(obj: object) -> Callable[[Container], bool]:
    """
    Utility function for checking whether the input contains a certain element,
    e.g. a string within a string, an object in a list, a key in a dict, etc.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.contains("456"),
        )
        assert schema.validate("123456789") == "123456789"
        schema.validate("987654321")  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    .. code-block:: python

        schema = validate.Schema(
            validate.contains(456),
        )
        assert schema.validate([123, 456, 789]) == [123, 456, 789]
        schema.validate([987, 654, 321])  # raises ValidationError
        schema.validate(None)  # raises ValidationError

    :raise ValidationError: If input is not an instance of :class:`collections.abc.Container`
    :raise ValidationError: If input doesn't contain ``obj``
    """

    def contains_str(value):
        validate(Container, value)
        if obj not in value:
            raise ValidationError(
                "{value} does not contain {obj}",
                value=repr(value),
                obj=repr(obj),
                schema="contains",
            )

        return False

    return contains_str

x_validator_contains__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_contains__mutmut_1': x_validator_contains__mutmut_1, 
    'x_validator_contains__mutmut_2': x_validator_contains__mutmut_2, 
    'x_validator_contains__mutmut_3': x_validator_contains__mutmut_3, 
    'x_validator_contains__mutmut_4': x_validator_contains__mutmut_4, 
    'x_validator_contains__mutmut_5': x_validator_contains__mutmut_5, 
    'x_validator_contains__mutmut_6': x_validator_contains__mutmut_6, 
    'x_validator_contains__mutmut_7': x_validator_contains__mutmut_7, 
    'x_validator_contains__mutmut_8': x_validator_contains__mutmut_8, 
    'x_validator_contains__mutmut_9': x_validator_contains__mutmut_9, 
    'x_validator_contains__mutmut_10': x_validator_contains__mutmut_10, 
    'x_validator_contains__mutmut_11': x_validator_contains__mutmut_11, 
    'x_validator_contains__mutmut_12': x_validator_contains__mutmut_12, 
    'x_validator_contains__mutmut_13': x_validator_contains__mutmut_13, 
    'x_validator_contains__mutmut_14': x_validator_contains__mutmut_14, 
    'x_validator_contains__mutmut_15': x_validator_contains__mutmut_15, 
    'x_validator_contains__mutmut_16': x_validator_contains__mutmut_16, 
    'x_validator_contains__mutmut_17': x_validator_contains__mutmut_17, 
    'x_validator_contains__mutmut_18': x_validator_contains__mutmut_18, 
    'x_validator_contains__mutmut_19': x_validator_contains__mutmut_19, 
    'x_validator_contains__mutmut_20': x_validator_contains__mutmut_20, 
    'x_validator_contains__mutmut_21': x_validator_contains__mutmut_21
}

def validator_contains(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_contains__mutmut_orig, x_validator_contains__mutmut_mutants, args, kwargs)
    return result 

validator_contains.__signature__ = _mutmut_signature(x_validator_contains__mutmut_orig)
x_validator_contains__mutmut_orig.__name__ = 'x_validator_contains'


def x_validator_url__mutmut_orig(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_1(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get(None) == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_2(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("XXschemeXX") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_3(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("SCHEME") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_4(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("Scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_5(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") != "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_6(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "XXhttpXX":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_7(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "HTTP":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_8(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "Http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_9(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = None

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_10(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["XXschemeXX"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_11(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["SCHEME"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_12(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["Scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_13(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema(None, "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_14(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", None)

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_15(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_16(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", )

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_17(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("XXhttpXX", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_18(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("HTTP", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_19(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("Http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_20(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "XXhttpsXX")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_21(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "HTTPS")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_22(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "Https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_23(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(None, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_24(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, None)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_25(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_26(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, )
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_27(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = None
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_28(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(None)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_29(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_30(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                None,
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_31(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=None,
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_32(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema=None,
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_33(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_34(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_35(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_36(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "XX{value} is not a valid URLXX",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_37(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid url",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_38(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{VALUE} IS NOT A VALID URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_39(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid url",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_40(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(None),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_41(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="XXurlXX",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_42(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="URL",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_43(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="Url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_44(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_45(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(None, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_46(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, None):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_47(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_48(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, ):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_49(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    None,
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_50(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=None,
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_51(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema=None,
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_52(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_53(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_54(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_55(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "XXInvalid URL attribute {name}XX",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_56(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "invalid url attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_57(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "INVALID URL ATTRIBUTE {NAME}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_58(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid url attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_59(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(None),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_60(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="XXurlXX",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_61(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="URL",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_62(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="Url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_63(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(None, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_64(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, None)
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_65(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_66(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, )
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_67(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(None, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_68(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, None))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_69(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_70(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, ))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_71(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    None,
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_72(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=None,
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_73(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema=None,
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_74(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_75(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_76(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    ) from err

        return True

    return check_url


def x_validator_url__mutmut_77(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "XXUnable to validate URL attribute {name}XX",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_78(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "unable to validate url attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_79(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "UNABLE TO VALIDATE URL ATTRIBUTE {NAME}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_80(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate url attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_81(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(None),
                    schema="url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_82(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="XXurlXX",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_83(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="URL",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_84(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="Url",
                ) from err

        return True

    return check_url


def x_validator_url__mutmut_85(**attributes) -> Callable[[str], bool]:
    """
    Utility function for validating a URL using schemas.

    Allows validating all URL attributes returned by :func:`urllib.parse.urlparse()`:

    - ``scheme`` - updated to ``AnySchema("http", "https")`` if set to ``"http"``
    - ``netloc``
    - ``path``
    - ``params``
    - ``query``
    - ``fragment``
    - ``username``
    - ``password``
    - ``hostname``
    - ``port``

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.url(path=validate.endswith(".m3u8")),
        )
        assert schema.validate("https://host/pl.m3u8?query") == "https://host/pl.m3u8?query"
        schema.validate(None)  # raises ValidationError
        schema.validate("not a URL")  # raises ValidationError
        schema.validate("https://host/no-pl?pl.m3u8")  # raises ValidationError

    :raise ValidationError: If input is not a string
    :raise ValidationError: If input is not a URL (doesn't have a ``netloc`` parsing result)
    :raise ValidationError: If an unknown URL attribute is passed as an option
    """

    # Convert "http" to AnySchema("http", "https") for convenience
    if attributes.get("scheme") == "http":
        attributes["scheme"] = AnySchema("http", "https")

    def check_url(value):
        validate(str, value)
        parsed = urlparse(value)
        if not parsed.netloc:
            raise ValidationError(
                "{value} is not a valid URL",
                value=repr(value),
                schema="url",
            )

        for name, schema in attributes.items():
            if not hasattr(parsed, name):
                raise ValidationError(
                    "Invalid URL attribute {name}",
                    name=repr(name),
                    schema="url",
                )

            try:
                validate(schema, getattr(parsed, name))
            except ValidationError as err:
                raise ValidationError(
                    "Unable to validate URL attribute {name}",
                    name=repr(name),
                    schema="url",
                ) from err

        return False

    return check_url

x_validator_url__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_url__mutmut_1': x_validator_url__mutmut_1, 
    'x_validator_url__mutmut_2': x_validator_url__mutmut_2, 
    'x_validator_url__mutmut_3': x_validator_url__mutmut_3, 
    'x_validator_url__mutmut_4': x_validator_url__mutmut_4, 
    'x_validator_url__mutmut_5': x_validator_url__mutmut_5, 
    'x_validator_url__mutmut_6': x_validator_url__mutmut_6, 
    'x_validator_url__mutmut_7': x_validator_url__mutmut_7, 
    'x_validator_url__mutmut_8': x_validator_url__mutmut_8, 
    'x_validator_url__mutmut_9': x_validator_url__mutmut_9, 
    'x_validator_url__mutmut_10': x_validator_url__mutmut_10, 
    'x_validator_url__mutmut_11': x_validator_url__mutmut_11, 
    'x_validator_url__mutmut_12': x_validator_url__mutmut_12, 
    'x_validator_url__mutmut_13': x_validator_url__mutmut_13, 
    'x_validator_url__mutmut_14': x_validator_url__mutmut_14, 
    'x_validator_url__mutmut_15': x_validator_url__mutmut_15, 
    'x_validator_url__mutmut_16': x_validator_url__mutmut_16, 
    'x_validator_url__mutmut_17': x_validator_url__mutmut_17, 
    'x_validator_url__mutmut_18': x_validator_url__mutmut_18, 
    'x_validator_url__mutmut_19': x_validator_url__mutmut_19, 
    'x_validator_url__mutmut_20': x_validator_url__mutmut_20, 
    'x_validator_url__mutmut_21': x_validator_url__mutmut_21, 
    'x_validator_url__mutmut_22': x_validator_url__mutmut_22, 
    'x_validator_url__mutmut_23': x_validator_url__mutmut_23, 
    'x_validator_url__mutmut_24': x_validator_url__mutmut_24, 
    'x_validator_url__mutmut_25': x_validator_url__mutmut_25, 
    'x_validator_url__mutmut_26': x_validator_url__mutmut_26, 
    'x_validator_url__mutmut_27': x_validator_url__mutmut_27, 
    'x_validator_url__mutmut_28': x_validator_url__mutmut_28, 
    'x_validator_url__mutmut_29': x_validator_url__mutmut_29, 
    'x_validator_url__mutmut_30': x_validator_url__mutmut_30, 
    'x_validator_url__mutmut_31': x_validator_url__mutmut_31, 
    'x_validator_url__mutmut_32': x_validator_url__mutmut_32, 
    'x_validator_url__mutmut_33': x_validator_url__mutmut_33, 
    'x_validator_url__mutmut_34': x_validator_url__mutmut_34, 
    'x_validator_url__mutmut_35': x_validator_url__mutmut_35, 
    'x_validator_url__mutmut_36': x_validator_url__mutmut_36, 
    'x_validator_url__mutmut_37': x_validator_url__mutmut_37, 
    'x_validator_url__mutmut_38': x_validator_url__mutmut_38, 
    'x_validator_url__mutmut_39': x_validator_url__mutmut_39, 
    'x_validator_url__mutmut_40': x_validator_url__mutmut_40, 
    'x_validator_url__mutmut_41': x_validator_url__mutmut_41, 
    'x_validator_url__mutmut_42': x_validator_url__mutmut_42, 
    'x_validator_url__mutmut_43': x_validator_url__mutmut_43, 
    'x_validator_url__mutmut_44': x_validator_url__mutmut_44, 
    'x_validator_url__mutmut_45': x_validator_url__mutmut_45, 
    'x_validator_url__mutmut_46': x_validator_url__mutmut_46, 
    'x_validator_url__mutmut_47': x_validator_url__mutmut_47, 
    'x_validator_url__mutmut_48': x_validator_url__mutmut_48, 
    'x_validator_url__mutmut_49': x_validator_url__mutmut_49, 
    'x_validator_url__mutmut_50': x_validator_url__mutmut_50, 
    'x_validator_url__mutmut_51': x_validator_url__mutmut_51, 
    'x_validator_url__mutmut_52': x_validator_url__mutmut_52, 
    'x_validator_url__mutmut_53': x_validator_url__mutmut_53, 
    'x_validator_url__mutmut_54': x_validator_url__mutmut_54, 
    'x_validator_url__mutmut_55': x_validator_url__mutmut_55, 
    'x_validator_url__mutmut_56': x_validator_url__mutmut_56, 
    'x_validator_url__mutmut_57': x_validator_url__mutmut_57, 
    'x_validator_url__mutmut_58': x_validator_url__mutmut_58, 
    'x_validator_url__mutmut_59': x_validator_url__mutmut_59, 
    'x_validator_url__mutmut_60': x_validator_url__mutmut_60, 
    'x_validator_url__mutmut_61': x_validator_url__mutmut_61, 
    'x_validator_url__mutmut_62': x_validator_url__mutmut_62, 
    'x_validator_url__mutmut_63': x_validator_url__mutmut_63, 
    'x_validator_url__mutmut_64': x_validator_url__mutmut_64, 
    'x_validator_url__mutmut_65': x_validator_url__mutmut_65, 
    'x_validator_url__mutmut_66': x_validator_url__mutmut_66, 
    'x_validator_url__mutmut_67': x_validator_url__mutmut_67, 
    'x_validator_url__mutmut_68': x_validator_url__mutmut_68, 
    'x_validator_url__mutmut_69': x_validator_url__mutmut_69, 
    'x_validator_url__mutmut_70': x_validator_url__mutmut_70, 
    'x_validator_url__mutmut_71': x_validator_url__mutmut_71, 
    'x_validator_url__mutmut_72': x_validator_url__mutmut_72, 
    'x_validator_url__mutmut_73': x_validator_url__mutmut_73, 
    'x_validator_url__mutmut_74': x_validator_url__mutmut_74, 
    'x_validator_url__mutmut_75': x_validator_url__mutmut_75, 
    'x_validator_url__mutmut_76': x_validator_url__mutmut_76, 
    'x_validator_url__mutmut_77': x_validator_url__mutmut_77, 
    'x_validator_url__mutmut_78': x_validator_url__mutmut_78, 
    'x_validator_url__mutmut_79': x_validator_url__mutmut_79, 
    'x_validator_url__mutmut_80': x_validator_url__mutmut_80, 
    'x_validator_url__mutmut_81': x_validator_url__mutmut_81, 
    'x_validator_url__mutmut_82': x_validator_url__mutmut_82, 
    'x_validator_url__mutmut_83': x_validator_url__mutmut_83, 
    'x_validator_url__mutmut_84': x_validator_url__mutmut_84, 
    'x_validator_url__mutmut_85': x_validator_url__mutmut_85
}

def validator_url(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_url__mutmut_orig, x_validator_url__mutmut_mutants, args, kwargs)
    return result 

validator_url.__signature__ = _mutmut_signature(x_validator_url__mutmut_orig)
x_validator_url__mutmut_orig.__name__ = 'x_validator_url'


# Object related validators


def x_validator_getattr__mutmut_orig(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, attr, default)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_1(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(None, attr, default)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_2(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, None, default)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_3(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, attr, None)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_4(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(attr, default)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_5(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, default)

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_6(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, attr, )

    return TransformSchema(getter)


# Object related validators


def x_validator_getattr__mutmut_7(attr: Any, default: Any = None) -> TransformSchema:
    """
    Utility function for getting an attribute from the input object.

    If a default is set, it is returned when the attribute doesn't exist.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.getattr("year", "unknown"),
        )
        assert schema.validate(datetime.date.fromisoformat("2000-01-01")) == 2000
        assert schema.validate("not a date/datetime object") == "unknown"
    """

    def getter(value):
        return getattr(value, attr, default)

    return TransformSchema(None)

x_validator_getattr__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_getattr__mutmut_1': x_validator_getattr__mutmut_1, 
    'x_validator_getattr__mutmut_2': x_validator_getattr__mutmut_2, 
    'x_validator_getattr__mutmut_3': x_validator_getattr__mutmut_3, 
    'x_validator_getattr__mutmut_4': x_validator_getattr__mutmut_4, 
    'x_validator_getattr__mutmut_5': x_validator_getattr__mutmut_5, 
    'x_validator_getattr__mutmut_6': x_validator_getattr__mutmut_6, 
    'x_validator_getattr__mutmut_7': x_validator_getattr__mutmut_7
}

def validator_getattr(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_getattr__mutmut_orig, x_validator_getattr__mutmut_mutants, args, kwargs)
    return result 

validator_getattr.__signature__ = _mutmut_signature(x_validator_getattr__mutmut_orig)
x_validator_getattr__mutmut_orig.__name__ = 'x_validator_getattr'


def x_validator_hasattr__mutmut_orig(attr: Any) -> Callable[[Any], bool]:
    """
    Utility function for checking whether an attribute exists on the input object.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.hasattr("year"),
        )
        date = datetime.date.fromisoformat("2000-01-01")
        assert schema.validate(date) is date
        schema.validate("not a date/datetime object")  # raises ValidationError
    """

    def getter(value):
        return hasattr(value, attr)

    return getter


def x_validator_hasattr__mutmut_1(attr: Any) -> Callable[[Any], bool]:
    """
    Utility function for checking whether an attribute exists on the input object.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.hasattr("year"),
        )
        date = datetime.date.fromisoformat("2000-01-01")
        assert schema.validate(date) is date
        schema.validate("not a date/datetime object")  # raises ValidationError
    """

    def getter(value):
        return hasattr(None, attr)

    return getter


def x_validator_hasattr__mutmut_2(attr: Any) -> Callable[[Any], bool]:
    """
    Utility function for checking whether an attribute exists on the input object.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.hasattr("year"),
        )
        date = datetime.date.fromisoformat("2000-01-01")
        assert schema.validate(date) is date
        schema.validate("not a date/datetime object")  # raises ValidationError
    """

    def getter(value):
        return hasattr(value, None)

    return getter


def x_validator_hasattr__mutmut_3(attr: Any) -> Callable[[Any], bool]:
    """
    Utility function for checking whether an attribute exists on the input object.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.hasattr("year"),
        )
        date = datetime.date.fromisoformat("2000-01-01")
        assert schema.validate(date) is date
        schema.validate("not a date/datetime object")  # raises ValidationError
    """

    def getter(value):
        return hasattr(attr)

    return getter


def x_validator_hasattr__mutmut_4(attr: Any) -> Callable[[Any], bool]:
    """
    Utility function for checking whether an attribute exists on the input object.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.hasattr("year"),
        )
        date = datetime.date.fromisoformat("2000-01-01")
        assert schema.validate(date) is date
        schema.validate("not a date/datetime object")  # raises ValidationError
    """

    def getter(value):
        return hasattr(value, )

    return getter

x_validator_hasattr__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_hasattr__mutmut_1': x_validator_hasattr__mutmut_1, 
    'x_validator_hasattr__mutmut_2': x_validator_hasattr__mutmut_2, 
    'x_validator_hasattr__mutmut_3': x_validator_hasattr__mutmut_3, 
    'x_validator_hasattr__mutmut_4': x_validator_hasattr__mutmut_4
}

def validator_hasattr(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_hasattr__mutmut_orig, x_validator_hasattr__mutmut_mutants, args, kwargs)
    return result 

validator_hasattr.__signature__ = _mutmut_signature(x_validator_hasattr__mutmut_orig)
x_validator_hasattr__mutmut_orig.__name__ = 'x_validator_hasattr'


# Sequence related validators


def x_validator_filter__mutmut_orig(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_1(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = None
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_2(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(None)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_3(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(None)
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_4(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(None, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_5(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, None))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_6(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_7(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, ))
        else:
            return cls(filter(func, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_8(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(None)

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_9(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(None, value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_10(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, None))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_11(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(value))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_12(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, ))

    return TransformSchema(filter_values)


# Sequence related validators


def x_validator_filter__mutmut_13(func: Callable[..., bool]) -> TransformSchema:
    """
    Utility function for filtering out unwanted items from the input using the specified function
    via the built-in :func:`filter() <builtins.filter>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda val: val < 3),
        )
        assert schema.validate([1, 2, 3, 4]) == [1, 2]

    .. code-block:: python

        schema = validate.Schema(
            validate.filter(lambda key, val: key > 1 and val < 3),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {2: 2}
    """

    def expand_kv(kv):
        return func(*kv)

    def filter_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(filter(expand_kv, value.items()))
        else:
            return cls(filter(func, value))

    return TransformSchema(None)

x_validator_filter__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_filter__mutmut_1': x_validator_filter__mutmut_1, 
    'x_validator_filter__mutmut_2': x_validator_filter__mutmut_2, 
    'x_validator_filter__mutmut_3': x_validator_filter__mutmut_3, 
    'x_validator_filter__mutmut_4': x_validator_filter__mutmut_4, 
    'x_validator_filter__mutmut_5': x_validator_filter__mutmut_5, 
    'x_validator_filter__mutmut_6': x_validator_filter__mutmut_6, 
    'x_validator_filter__mutmut_7': x_validator_filter__mutmut_7, 
    'x_validator_filter__mutmut_8': x_validator_filter__mutmut_8, 
    'x_validator_filter__mutmut_9': x_validator_filter__mutmut_9, 
    'x_validator_filter__mutmut_10': x_validator_filter__mutmut_10, 
    'x_validator_filter__mutmut_11': x_validator_filter__mutmut_11, 
    'x_validator_filter__mutmut_12': x_validator_filter__mutmut_12, 
    'x_validator_filter__mutmut_13': x_validator_filter__mutmut_13
}

def validator_filter(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_filter__mutmut_orig, x_validator_filter__mutmut_mutants, args, kwargs)
    return result 

validator_filter.__signature__ = _mutmut_signature(x_validator_filter__mutmut_orig)
x_validator_filter__mutmut_orig.__name__ = 'x_validator_filter'


def x_validator_map__mutmut_orig(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_1(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = None
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_2(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(None)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_3(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(None)
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_4(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(None, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_5(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, None))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_6(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_7(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, ))
        else:
            return cls(map(func, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_8(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(None)

    return TransformSchema(map_values)


def x_validator_map__mutmut_9(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(None, value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_10(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, None))

    return TransformSchema(map_values)


def x_validator_map__mutmut_11(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(value))

    return TransformSchema(map_values)


def x_validator_map__mutmut_12(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, ))

    return TransformSchema(map_values)


def x_validator_map__mutmut_13(func: Callable[..., Any]) -> TransformSchema:
    """
    Utility function for mapping/transforming items from the input using the specified function,
    via the built-in :func:`map() <builtins.map>`.

    Supports iterables, as well as instances of :class:`dict` where key-value pairs are expanded.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda val: val + 1),
        )
        assert schema.validate([1, 2, 3, 4]) == [2, 3, 4, 5]

    .. code-block:: python

        schema = validate.Schema(
            validate.map(lambda key, val: (key + 1, val * 2)),
        )
        assert schema.validate({0: 0, 1: 1, 2: 2, 3: 3, 4: 4}) == {1: 0, 2: 2, 3: 4, 4: 6, 5: 8}
    """

    def expand_kv(kv):
        return func(*kv)

    def map_values(value):
        cls = type(value)
        if isinstance(value, dict):
            return cls(map(expand_kv, value.items()))
        else:
            return cls(map(func, value))

    return TransformSchema(None)

x_validator_map__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_map__mutmut_1': x_validator_map__mutmut_1, 
    'x_validator_map__mutmut_2': x_validator_map__mutmut_2, 
    'x_validator_map__mutmut_3': x_validator_map__mutmut_3, 
    'x_validator_map__mutmut_4': x_validator_map__mutmut_4, 
    'x_validator_map__mutmut_5': x_validator_map__mutmut_5, 
    'x_validator_map__mutmut_6': x_validator_map__mutmut_6, 
    'x_validator_map__mutmut_7': x_validator_map__mutmut_7, 
    'x_validator_map__mutmut_8': x_validator_map__mutmut_8, 
    'x_validator_map__mutmut_9': x_validator_map__mutmut_9, 
    'x_validator_map__mutmut_10': x_validator_map__mutmut_10, 
    'x_validator_map__mutmut_11': x_validator_map__mutmut_11, 
    'x_validator_map__mutmut_12': x_validator_map__mutmut_12, 
    'x_validator_map__mutmut_13': x_validator_map__mutmut_13
}

def validator_map(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_map__mutmut_orig, x_validator_map__mutmut_mutants, args, kwargs)
    return result 

validator_map.__signature__ = _mutmut_signature(x_validator_map__mutmut_orig)
x_validator_map__mutmut_orig.__name__ = 'x_validator_map'


# lxml.etree related validators


def x_validator_xml_find__mutmut_orig(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_1(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(None, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_2(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, None)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_3(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_4(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, )

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_5(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = None
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_6(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(None, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_7(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=None)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_8(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_9(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, )
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_10(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.rfind(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_11(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                None,
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_12(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=None,
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_13(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema=None,
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_14(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_15(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_16(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_17(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "XXElementPath syntax error: {path}XX",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_18(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "elementpath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_19(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ELEMENTPATH SYNTAX ERROR: {PATH}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_20(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "Elementpath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_21(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(None),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_22(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="XXxml_findXX",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_23(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="XML_FIND",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_24(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="Xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_25(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is not None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_26(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                None,
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_27(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=None,
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_28(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema=None,
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_29(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_30(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_31(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_32(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "XXElementPath query {path} did not return an elementXX",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_33(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "elementpath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_34(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ELEMENTPATH QUERY {PATH} DID NOT RETURN AN ELEMENT",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_35(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "Elementpath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_36(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(None),
                schema="xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_37(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="XXxml_findXX",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_38(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="XML_FIND",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_39(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="Xml_find",
            )

        return value

    return TransformSchema(xpath_find)


# lxml.etree related validators


def x_validator_xml_find__mutmut_40(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_find(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")).text == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    def xpath_find(value):
        validate(iselement, value)

        try:
            value = value.find(path, namespaces=namespaces)
        except SyntaxError as err:
            raise ValidationError(
                "ElementPath syntax error: {path}",
                path=repr(path),
                schema="xml_find",
            ) from err

        if value is None:
            raise ValidationError(
                "ElementPath query {path} did not return an element",
                path=repr(path),
                schema="xml_find",
            )

        return value

    return TransformSchema(None)

x_validator_xml_find__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_xml_find__mutmut_1': x_validator_xml_find__mutmut_1, 
    'x_validator_xml_find__mutmut_2': x_validator_xml_find__mutmut_2, 
    'x_validator_xml_find__mutmut_3': x_validator_xml_find__mutmut_3, 
    'x_validator_xml_find__mutmut_4': x_validator_xml_find__mutmut_4, 
    'x_validator_xml_find__mutmut_5': x_validator_xml_find__mutmut_5, 
    'x_validator_xml_find__mutmut_6': x_validator_xml_find__mutmut_6, 
    'x_validator_xml_find__mutmut_7': x_validator_xml_find__mutmut_7, 
    'x_validator_xml_find__mutmut_8': x_validator_xml_find__mutmut_8, 
    'x_validator_xml_find__mutmut_9': x_validator_xml_find__mutmut_9, 
    'x_validator_xml_find__mutmut_10': x_validator_xml_find__mutmut_10, 
    'x_validator_xml_find__mutmut_11': x_validator_xml_find__mutmut_11, 
    'x_validator_xml_find__mutmut_12': x_validator_xml_find__mutmut_12, 
    'x_validator_xml_find__mutmut_13': x_validator_xml_find__mutmut_13, 
    'x_validator_xml_find__mutmut_14': x_validator_xml_find__mutmut_14, 
    'x_validator_xml_find__mutmut_15': x_validator_xml_find__mutmut_15, 
    'x_validator_xml_find__mutmut_16': x_validator_xml_find__mutmut_16, 
    'x_validator_xml_find__mutmut_17': x_validator_xml_find__mutmut_17, 
    'x_validator_xml_find__mutmut_18': x_validator_xml_find__mutmut_18, 
    'x_validator_xml_find__mutmut_19': x_validator_xml_find__mutmut_19, 
    'x_validator_xml_find__mutmut_20': x_validator_xml_find__mutmut_20, 
    'x_validator_xml_find__mutmut_21': x_validator_xml_find__mutmut_21, 
    'x_validator_xml_find__mutmut_22': x_validator_xml_find__mutmut_22, 
    'x_validator_xml_find__mutmut_23': x_validator_xml_find__mutmut_23, 
    'x_validator_xml_find__mutmut_24': x_validator_xml_find__mutmut_24, 
    'x_validator_xml_find__mutmut_25': x_validator_xml_find__mutmut_25, 
    'x_validator_xml_find__mutmut_26': x_validator_xml_find__mutmut_26, 
    'x_validator_xml_find__mutmut_27': x_validator_xml_find__mutmut_27, 
    'x_validator_xml_find__mutmut_28': x_validator_xml_find__mutmut_28, 
    'x_validator_xml_find__mutmut_29': x_validator_xml_find__mutmut_29, 
    'x_validator_xml_find__mutmut_30': x_validator_xml_find__mutmut_30, 
    'x_validator_xml_find__mutmut_31': x_validator_xml_find__mutmut_31, 
    'x_validator_xml_find__mutmut_32': x_validator_xml_find__mutmut_32, 
    'x_validator_xml_find__mutmut_33': x_validator_xml_find__mutmut_33, 
    'x_validator_xml_find__mutmut_34': x_validator_xml_find__mutmut_34, 
    'x_validator_xml_find__mutmut_35': x_validator_xml_find__mutmut_35, 
    'x_validator_xml_find__mutmut_36': x_validator_xml_find__mutmut_36, 
    'x_validator_xml_find__mutmut_37': x_validator_xml_find__mutmut_37, 
    'x_validator_xml_find__mutmut_38': x_validator_xml_find__mutmut_38, 
    'x_validator_xml_find__mutmut_39': x_validator_xml_find__mutmut_39, 
    'x_validator_xml_find__mutmut_40': x_validator_xml_find__mutmut_40
}

def validator_xml_find(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_xml_find__mutmut_orig, x_validator_xml_find__mutmut_mutants, args, kwargs)
    return result 

validator_xml_find.__signature__ = _mutmut_signature(x_validator_xml_find__mutmut_orig)
x_validator_xml_find__mutmut_orig.__name__ = 'x_validator_xml_find'


def x_validator_xml_findall__mutmut_orig(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_1(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(None, value)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_2(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, None)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_3(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(value)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_4(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, )
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_5(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(None, namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_6(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(path, namespaces=None)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_7(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(namespaces=namespaces)

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_8(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(path, )

    return TransformSchema(xpath_findall)


def x_validator_xml_findall__mutmut_9(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> TransformSchema:
    """
    Utility function for finding XML elements using :meth:`Element.findall()`.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findall(".//b"),
            validate.map(lambda elem: elem.text),
        )
        assert schema.validate(lxml.etree.XML("<a><b>1</b><b>2</b></a>")) == ["1", "2"]
        assert schema.validate(lxml.etree.XML("<a><c></c></a>")) == []
        schema.validate("<a><b>1</b><b>2</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    """

    def xpath_findall(value):
        validate(iselement, value)
        return value.findall(path, namespaces=namespaces)

    return TransformSchema(None)

x_validator_xml_findall__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_xml_findall__mutmut_1': x_validator_xml_findall__mutmut_1, 
    'x_validator_xml_findall__mutmut_2': x_validator_xml_findall__mutmut_2, 
    'x_validator_xml_findall__mutmut_3': x_validator_xml_findall__mutmut_3, 
    'x_validator_xml_findall__mutmut_4': x_validator_xml_findall__mutmut_4, 
    'x_validator_xml_findall__mutmut_5': x_validator_xml_findall__mutmut_5, 
    'x_validator_xml_findall__mutmut_6': x_validator_xml_findall__mutmut_6, 
    'x_validator_xml_findall__mutmut_7': x_validator_xml_findall__mutmut_7, 
    'x_validator_xml_findall__mutmut_8': x_validator_xml_findall__mutmut_8, 
    'x_validator_xml_findall__mutmut_9': x_validator_xml_findall__mutmut_9
}

def validator_xml_findall(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_xml_findall__mutmut_orig, x_validator_xml_findall__mutmut_mutants, args, kwargs)
    return result 

validator_xml_findall.__signature__ = _mutmut_signature(x_validator_xml_findall__mutmut_orig)
x_validator_xml_findall__mutmut_orig.__name__ = 'x_validator_xml_findall'


def x_validator_xml_findtext__mutmut_orig(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_1(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        None,
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_2(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        None,
    )


def x_validator_xml_findtext__mutmut_3(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_4(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        )


def x_validator_xml_findtext__mutmut_5(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(None, namespaces=namespaces),
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_6(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=None),
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_7(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(namespaces=namespaces),
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_8(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, ),
        validator_getattr("text"),
    )


def x_validator_xml_findtext__mutmut_9(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr(None),
    )


def x_validator_xml_findtext__mutmut_10(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr("XXtextXX"),
    )


def x_validator_xml_findtext__mutmut_11(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr("TEXT"),
    )


def x_validator_xml_findtext__mutmut_12(
    path: str,
    namespaces: Mapping[str, str] | None = None,
) -> AllSchema:
    """
    Utility function for finding an XML element using :meth:`Element.find()` and returning its ``text`` attribute.

    This method uses the ElementPath query language, which is a subset of XPath.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_findtext(".//b/c"),
        )
        assert schema.validate(lxml.etree.XML("<a><b><c>d</c></b></a>")) == "d"
        schema.validate(lxml.etree.XML("<a><b></b></a>"))  # raises ValidationError
        schema.validate("<a><b><c>d</c></b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On ElementPath evaluation error
    :raise ValidationError: If the query didn't return an XML element
    """

    return AllSchema(
        validator_xml_find(path, namespaces=namespaces),
        validator_getattr("Text"),
    )

x_validator_xml_findtext__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_xml_findtext__mutmut_1': x_validator_xml_findtext__mutmut_1, 
    'x_validator_xml_findtext__mutmut_2': x_validator_xml_findtext__mutmut_2, 
    'x_validator_xml_findtext__mutmut_3': x_validator_xml_findtext__mutmut_3, 
    'x_validator_xml_findtext__mutmut_4': x_validator_xml_findtext__mutmut_4, 
    'x_validator_xml_findtext__mutmut_5': x_validator_xml_findtext__mutmut_5, 
    'x_validator_xml_findtext__mutmut_6': x_validator_xml_findtext__mutmut_6, 
    'x_validator_xml_findtext__mutmut_7': x_validator_xml_findtext__mutmut_7, 
    'x_validator_xml_findtext__mutmut_8': x_validator_xml_findtext__mutmut_8, 
    'x_validator_xml_findtext__mutmut_9': x_validator_xml_findtext__mutmut_9, 
    'x_validator_xml_findtext__mutmut_10': x_validator_xml_findtext__mutmut_10, 
    'x_validator_xml_findtext__mutmut_11': x_validator_xml_findtext__mutmut_11, 
    'x_validator_xml_findtext__mutmut_12': x_validator_xml_findtext__mutmut_12
}

def validator_xml_findtext(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_xml_findtext__mutmut_orig, x_validator_xml_findtext__mutmut_mutants, args, kwargs)
    return result 

validator_xml_findtext.__signature__ = _mutmut_signature(x_validator_xml_findtext__mutmut_orig)
x_validator_xml_findtext__mutmut_orig.__name__ = 'x_validator_xml_findtext'


def x_validator_xml_xpath__mutmut_orig(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_1(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = False,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_2(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(None, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_3(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, None)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_4(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_5(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, )
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_6(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = None
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_7(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                None,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_8(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=None,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_9(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=None,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_10(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=None,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_11(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_12(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_13(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_14(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_15(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_16(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                None,
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_17(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=None,
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_18(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema=None,
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_19(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_20(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_21(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_22(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XXXPath evaluation error: {xpath}XX",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_23(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "xpath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_24(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPATH EVALUATION ERROR: {XPATH}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_25(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "Xpath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_26(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(None),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_27(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="XXxml_xpathXX",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_28(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="XML_XPATH",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_29(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="Xml_xpath",
            ) from err

        return result or None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_30(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result and None

    return TransformSchema(transform_xpath)


def x_validator_xml_xpath__mutmut_31(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    smart_strings: bool = True,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`).

    XPath queries always return a result set, but if the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath(".//b[@c=$c][1]/@d", c="2"),
        )
        assert schema.validate(lxml.etree.XML("<a><b c='1' d='A'/><b c='2' d='B'/></a>")) == ["B"]
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b c='1' d='A'/><b c='2' d='B'/></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    def transform_xpath(value):
        validate(iselement, value)
        try:
            result = value.xpath(
                xpath,
                namespaces=namespaces,
                extensions=extensions,
                smart_strings=smart_strings,
                **variables,
            )
        except XPathError as err:
            raise ValidationError(
                "XPath evaluation error: {xpath}",
                xpath=repr(xpath),
                schema="xml_xpath",
            ) from err

        return result or None

    return TransformSchema(None)

x_validator_xml_xpath__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_xml_xpath__mutmut_1': x_validator_xml_xpath__mutmut_1, 
    'x_validator_xml_xpath__mutmut_2': x_validator_xml_xpath__mutmut_2, 
    'x_validator_xml_xpath__mutmut_3': x_validator_xml_xpath__mutmut_3, 
    'x_validator_xml_xpath__mutmut_4': x_validator_xml_xpath__mutmut_4, 
    'x_validator_xml_xpath__mutmut_5': x_validator_xml_xpath__mutmut_5, 
    'x_validator_xml_xpath__mutmut_6': x_validator_xml_xpath__mutmut_6, 
    'x_validator_xml_xpath__mutmut_7': x_validator_xml_xpath__mutmut_7, 
    'x_validator_xml_xpath__mutmut_8': x_validator_xml_xpath__mutmut_8, 
    'x_validator_xml_xpath__mutmut_9': x_validator_xml_xpath__mutmut_9, 
    'x_validator_xml_xpath__mutmut_10': x_validator_xml_xpath__mutmut_10, 
    'x_validator_xml_xpath__mutmut_11': x_validator_xml_xpath__mutmut_11, 
    'x_validator_xml_xpath__mutmut_12': x_validator_xml_xpath__mutmut_12, 
    'x_validator_xml_xpath__mutmut_13': x_validator_xml_xpath__mutmut_13, 
    'x_validator_xml_xpath__mutmut_14': x_validator_xml_xpath__mutmut_14, 
    'x_validator_xml_xpath__mutmut_15': x_validator_xml_xpath__mutmut_15, 
    'x_validator_xml_xpath__mutmut_16': x_validator_xml_xpath__mutmut_16, 
    'x_validator_xml_xpath__mutmut_17': x_validator_xml_xpath__mutmut_17, 
    'x_validator_xml_xpath__mutmut_18': x_validator_xml_xpath__mutmut_18, 
    'x_validator_xml_xpath__mutmut_19': x_validator_xml_xpath__mutmut_19, 
    'x_validator_xml_xpath__mutmut_20': x_validator_xml_xpath__mutmut_20, 
    'x_validator_xml_xpath__mutmut_21': x_validator_xml_xpath__mutmut_21, 
    'x_validator_xml_xpath__mutmut_22': x_validator_xml_xpath__mutmut_22, 
    'x_validator_xml_xpath__mutmut_23': x_validator_xml_xpath__mutmut_23, 
    'x_validator_xml_xpath__mutmut_24': x_validator_xml_xpath__mutmut_24, 
    'x_validator_xml_xpath__mutmut_25': x_validator_xml_xpath__mutmut_25, 
    'x_validator_xml_xpath__mutmut_26': x_validator_xml_xpath__mutmut_26, 
    'x_validator_xml_xpath__mutmut_27': x_validator_xml_xpath__mutmut_27, 
    'x_validator_xml_xpath__mutmut_28': x_validator_xml_xpath__mutmut_28, 
    'x_validator_xml_xpath__mutmut_29': x_validator_xml_xpath__mutmut_29, 
    'x_validator_xml_xpath__mutmut_30': x_validator_xml_xpath__mutmut_30, 
    'x_validator_xml_xpath__mutmut_31': x_validator_xml_xpath__mutmut_31
}

def validator_xml_xpath(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_xml_xpath__mutmut_orig, x_validator_xml_xpath__mutmut_mutants, args, kwargs)
    return result 

validator_xml_xpath.__signature__ = _mutmut_signature(x_validator_xml_xpath__mutmut_orig)
x_validator_xml_xpath__mutmut_orig.__name__ = 'x_validator_xml_xpath'


def x_validator_xml_xpath_string__mutmut_orig(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_1(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        None,
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_2(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=None,
        extensions=extensions,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_3(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=None,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_4(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=None,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_5(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_6(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        extensions=extensions,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_7(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        smart_strings=False,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_8(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=extensions,
        **variables,
    )


def x_validator_xml_xpath_string__mutmut_9(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=False,
        )


def x_validator_xml_xpath_string__mutmut_10(
    xpath: str,
    namespaces: Mapping[str, str] | None = None,
    extensions: Mapping[tuple[str | None, str], Callable[..., Any]] | None = None,
    **variables,
) -> TransformSchema:
    """
    Utility function for querying XML elements using XPath (:meth:`Element.xpath()`) and turning the result into a string.

    XPath queries always return a result set, so be aware when querying multiple elements.
    If the result is an empty set, this function instead returns ``None``.

    Allows setting XPath variables (``$var``) as additional keywords.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.xml_xpath_string(".//b[2]/text()"),
        )
        assert schema.validate(lxml.etree.XML("<a><b>A</b><b>B</b><b>C</b></a>")) == "B"
        assert schema.validate(lxml.etree.XML("<a></a>")) is None
        schema.validate("<a><b>A</b><b>B</b><b>C</b></a>")  # raises ValidationError

    :raise ValidationError: If the input is not an :class:`lxml.etree.Element`
    :raise ValidationError: On XPath evaluation error
    """

    return validator_xml_xpath(
        f"string({xpath})",
        namespaces=namespaces,
        extensions=extensions,
        smart_strings=True,
        **variables,
    )

x_validator_xml_xpath_string__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_xml_xpath_string__mutmut_1': x_validator_xml_xpath_string__mutmut_1, 
    'x_validator_xml_xpath_string__mutmut_2': x_validator_xml_xpath_string__mutmut_2, 
    'x_validator_xml_xpath_string__mutmut_3': x_validator_xml_xpath_string__mutmut_3, 
    'x_validator_xml_xpath_string__mutmut_4': x_validator_xml_xpath_string__mutmut_4, 
    'x_validator_xml_xpath_string__mutmut_5': x_validator_xml_xpath_string__mutmut_5, 
    'x_validator_xml_xpath_string__mutmut_6': x_validator_xml_xpath_string__mutmut_6, 
    'x_validator_xml_xpath_string__mutmut_7': x_validator_xml_xpath_string__mutmut_7, 
    'x_validator_xml_xpath_string__mutmut_8': x_validator_xml_xpath_string__mutmut_8, 
    'x_validator_xml_xpath_string__mutmut_9': x_validator_xml_xpath_string__mutmut_9, 
    'x_validator_xml_xpath_string__mutmut_10': x_validator_xml_xpath_string__mutmut_10
}

def validator_xml_xpath_string(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_xml_xpath_string__mutmut_orig, x_validator_xml_xpath_string__mutmut_mutants, args, kwargs)
    return result 

validator_xml_xpath_string.__signature__ = _mutmut_signature(x_validator_xml_xpath_string__mutmut_orig)
x_validator_xml_xpath_string__mutmut_orig.__name__ = 'x_validator_xml_xpath_string'


# Parse utility related validators


def x_validator_parse_json__mutmut_orig(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, *args, **kwargs, exception=ValidationError, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_1(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(None, *args, **kwargs, exception=ValidationError, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_2(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, *args, **kwargs, exception=None, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_3(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(*args, **kwargs, exception=ValidationError, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_4(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, **kwargs, exception=ValidationError, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_5(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, *args, exception=ValidationError, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_6(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, *args, **kwargs, schema=None)


# Parse utility related validators


def x_validator_parse_json__mutmut_7(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing JSON data using :func:`streamlink.utils.parse.parse_json()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_json(),
        )
        assert schema.validate(\"\"\"{"a":[1,2,3],"b":null}\"\"\") == {"a": [1, 2, 3], "b": None}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_json, *args, **kwargs, exception=ValidationError, )

x_validator_parse_json__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_parse_json__mutmut_1': x_validator_parse_json__mutmut_1, 
    'x_validator_parse_json__mutmut_2': x_validator_parse_json__mutmut_2, 
    'x_validator_parse_json__mutmut_3': x_validator_parse_json__mutmut_3, 
    'x_validator_parse_json__mutmut_4': x_validator_parse_json__mutmut_4, 
    'x_validator_parse_json__mutmut_5': x_validator_parse_json__mutmut_5, 
    'x_validator_parse_json__mutmut_6': x_validator_parse_json__mutmut_6, 
    'x_validator_parse_json__mutmut_7': x_validator_parse_json__mutmut_7
}

def validator_parse_json(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_parse_json__mutmut_orig, x_validator_parse_json__mutmut_mutants, args, kwargs)
    return result 

validator_parse_json.__signature__ = _mutmut_signature(x_validator_parse_json__mutmut_orig)
x_validator_parse_json__mutmut_orig.__name__ = 'x_validator_parse_json'


def x_validator_parse_html__mutmut_orig(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, *args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_html__mutmut_1(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(None, *args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_html__mutmut_2(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, *args, **kwargs, exception=None, schema=None)


def x_validator_parse_html__mutmut_3(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(*args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_html__mutmut_4(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_html__mutmut_5(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, *args, exception=ValidationError, schema=None)


def x_validator_parse_html__mutmut_6(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, *args, **kwargs, schema=None)


def x_validator_parse_html__mutmut_7(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing HTML data using :func:`streamlink.utils.parse.parse_html()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_html(),
        )
        assert schema.validate(\"\"\"<html lang="en">\"\"\").attrib["lang"] == "en"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_html, *args, **kwargs, exception=ValidationError, )

x_validator_parse_html__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_parse_html__mutmut_1': x_validator_parse_html__mutmut_1, 
    'x_validator_parse_html__mutmut_2': x_validator_parse_html__mutmut_2, 
    'x_validator_parse_html__mutmut_3': x_validator_parse_html__mutmut_3, 
    'x_validator_parse_html__mutmut_4': x_validator_parse_html__mutmut_4, 
    'x_validator_parse_html__mutmut_5': x_validator_parse_html__mutmut_5, 
    'x_validator_parse_html__mutmut_6': x_validator_parse_html__mutmut_6, 
    'x_validator_parse_html__mutmut_7': x_validator_parse_html__mutmut_7
}

def validator_parse_html(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_parse_html__mutmut_orig, x_validator_parse_html__mutmut_mutants, args, kwargs)
    return result 

validator_parse_html.__signature__ = _mutmut_signature(x_validator_parse_html__mutmut_orig)
x_validator_parse_html__mutmut_orig.__name__ = 'x_validator_parse_html'


def x_validator_parse_xml__mutmut_orig(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, *args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_xml__mutmut_1(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(None, *args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_xml__mutmut_2(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, *args, **kwargs, exception=None, schema=None)


def x_validator_parse_xml__mutmut_3(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(*args, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_xml__mutmut_4(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, **kwargs, exception=ValidationError, schema=None)


def x_validator_parse_xml__mutmut_5(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, *args, exception=ValidationError, schema=None)


def x_validator_parse_xml__mutmut_6(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, *args, **kwargs, schema=None)


def x_validator_parse_xml__mutmut_7(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing XML data using :func:`streamlink.utils.parse.parse_xml()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_xml(),
        )
        assert schema.validate(\"\"\"<a b="c"/>\"\"\").attrib["b"] == "c"
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    return TransformSchema(_parse_xml, *args, **kwargs, exception=ValidationError, )

x_validator_parse_xml__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_parse_xml__mutmut_1': x_validator_parse_xml__mutmut_1, 
    'x_validator_parse_xml__mutmut_2': x_validator_parse_xml__mutmut_2, 
    'x_validator_parse_xml__mutmut_3': x_validator_parse_xml__mutmut_3, 
    'x_validator_parse_xml__mutmut_4': x_validator_parse_xml__mutmut_4, 
    'x_validator_parse_xml__mutmut_5': x_validator_parse_xml__mutmut_5, 
    'x_validator_parse_xml__mutmut_6': x_validator_parse_xml__mutmut_6, 
    'x_validator_parse_xml__mutmut_7': x_validator_parse_xml__mutmut_7
}

def validator_parse_xml(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_parse_xml__mutmut_orig, x_validator_parse_xml__mutmut_mutants, args, kwargs)
    return result 

validator_parse_xml.__signature__ = _mutmut_signature(x_validator_parse_xml__mutmut_orig)
x_validator_parse_xml__mutmut_orig.__name__ = 'x_validator_parse_xml'


def x_validator_parse_qsd__mutmut_orig(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_1(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(None, _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_2(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), None)
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_3(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(_args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_4(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), )
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_5(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(None, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_6(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, None), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_7(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_8(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, ), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_9(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[1])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_10(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=None, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_11(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(**_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_12(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_13(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, schema=None)

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_14(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, )

    return TransformSchema(parser, *args, **kwargs)


def x_validator_parse_qsd__mutmut_15(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(None, *args, **kwargs)


def x_validator_parse_qsd__mutmut_16(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(*args, **kwargs)


def x_validator_parse_qsd__mutmut_17(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, **kwargs)


def x_validator_parse_qsd__mutmut_18(*args, **kwargs) -> TransformSchema:
    """
    Utility function for parsing a query string using :func:`streamlink.utils.parse.parse_qsd()`.

    Example:

    .. code-block:: python

        schema = validate.Schema(
            validate.parse_qsd(),
        )
        assert schema.validate("a=b&a=c&foo=bar") == {"a": "c", "foo": "bar"}
        schema.validate(123)  # raises ValidationError

    :raise ValidationError: On parsing error
    """

    def parser(*_args, **_kwargs):
        validate(AnySchema(str, bytes), _args[0])
        return _parse_qsd(*_args, **_kwargs, exception=ValidationError, schema=None)

    return TransformSchema(parser, *args, )

x_validator_parse_qsd__mutmut_mutants : ClassVar[MutantDict] = {
'x_validator_parse_qsd__mutmut_1': x_validator_parse_qsd__mutmut_1, 
    'x_validator_parse_qsd__mutmut_2': x_validator_parse_qsd__mutmut_2, 
    'x_validator_parse_qsd__mutmut_3': x_validator_parse_qsd__mutmut_3, 
    'x_validator_parse_qsd__mutmut_4': x_validator_parse_qsd__mutmut_4, 
    'x_validator_parse_qsd__mutmut_5': x_validator_parse_qsd__mutmut_5, 
    'x_validator_parse_qsd__mutmut_6': x_validator_parse_qsd__mutmut_6, 
    'x_validator_parse_qsd__mutmut_7': x_validator_parse_qsd__mutmut_7, 
    'x_validator_parse_qsd__mutmut_8': x_validator_parse_qsd__mutmut_8, 
    'x_validator_parse_qsd__mutmut_9': x_validator_parse_qsd__mutmut_9, 
    'x_validator_parse_qsd__mutmut_10': x_validator_parse_qsd__mutmut_10, 
    'x_validator_parse_qsd__mutmut_11': x_validator_parse_qsd__mutmut_11, 
    'x_validator_parse_qsd__mutmut_12': x_validator_parse_qsd__mutmut_12, 
    'x_validator_parse_qsd__mutmut_13': x_validator_parse_qsd__mutmut_13, 
    'x_validator_parse_qsd__mutmut_14': x_validator_parse_qsd__mutmut_14, 
    'x_validator_parse_qsd__mutmut_15': x_validator_parse_qsd__mutmut_15, 
    'x_validator_parse_qsd__mutmut_16': x_validator_parse_qsd__mutmut_16, 
    'x_validator_parse_qsd__mutmut_17': x_validator_parse_qsd__mutmut_17, 
    'x_validator_parse_qsd__mutmut_18': x_validator_parse_qsd__mutmut_18
}

def validator_parse_qsd(*args, **kwargs):
    result = _mutmut_trampoline(x_validator_parse_qsd__mutmut_orig, x_validator_parse_qsd__mutmut_mutants, args, kwargs)
    return result 

validator_parse_qsd.__signature__ = _mutmut_signature(x_validator_parse_qsd__mutmut_orig)
x_validator_parse_qsd__mutmut_orig.__name__ = 'x_validator_parse_qsd'

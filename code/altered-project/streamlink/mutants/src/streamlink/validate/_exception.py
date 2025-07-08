from __future__ import annotations

from collections.abc import Sequence
from textwrap import indent
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


class ValidationError(ValueError):
    """
    Currently not exposed in the public API.
    """

    MAX_LENGTH = 60

    errors: str | Exception | Sequence[str | Exception]

    def xǁValidationErrorǁ__init____mutmut_orig(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_1(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = None
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_2(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) != 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_3(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 2 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_4(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 or isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_5(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = None
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_6(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(None, **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_7(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(**errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_8(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], ),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_9(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[1], **errkeywords),)
        else:
            self.errors = errors

    def xǁValidationErrorǁ__init____mutmut_10(
        self,
        *errors,
        schema: str | object | None = None,
        **errkeywords,
    ):
        self.schema = schema
        if len(errors) == 1 and isinstance(errors[0], str):
            self.errors = (self._truncate(errors[0], **errkeywords),)
        else:
            self.errors = None
    
    xǁValidationErrorǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__init____mutmut_1': xǁValidationErrorǁ__init____mutmut_1, 
        'xǁValidationErrorǁ__init____mutmut_2': xǁValidationErrorǁ__init____mutmut_2, 
        'xǁValidationErrorǁ__init____mutmut_3': xǁValidationErrorǁ__init____mutmut_3, 
        'xǁValidationErrorǁ__init____mutmut_4': xǁValidationErrorǁ__init____mutmut_4, 
        'xǁValidationErrorǁ__init____mutmut_5': xǁValidationErrorǁ__init____mutmut_5, 
        'xǁValidationErrorǁ__init____mutmut_6': xǁValidationErrorǁ__init____mutmut_6, 
        'xǁValidationErrorǁ__init____mutmut_7': xǁValidationErrorǁ__init____mutmut_7, 
        'xǁValidationErrorǁ__init____mutmut_8': xǁValidationErrorǁ__init____mutmut_8, 
        'xǁValidationErrorǁ__init____mutmut_9': xǁValidationErrorǁ__init____mutmut_9, 
        'xǁValidationErrorǁ__init____mutmut_10': xǁValidationErrorǁ__init____mutmut_10
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__init____mutmut_orig)
    xǁValidationErrorǁ__init____mutmut_orig.__name__ = 'xǁValidationErrorǁ__init__'

    def xǁValidationErrorǁ_ellipsis__mutmut_orig(self, string: str):
        return string if len(string) <= self.MAX_LENGTH else f"<{string[: self.MAX_LENGTH - 5]}...>"

    def xǁValidationErrorǁ_ellipsis__mutmut_1(self, string: str):
        return string if len(string) < self.MAX_LENGTH else f"<{string[: self.MAX_LENGTH - 5]}...>"

    def xǁValidationErrorǁ_ellipsis__mutmut_2(self, string: str):
        return string if len(string) <= self.MAX_LENGTH else f"<{string[: self.MAX_LENGTH + 5]}...>"

    def xǁValidationErrorǁ_ellipsis__mutmut_3(self, string: str):
        return string if len(string) <= self.MAX_LENGTH else f"<{string[: self.MAX_LENGTH - 6]}...>"
    
    xǁValidationErrorǁ_ellipsis__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ_ellipsis__mutmut_1': xǁValidationErrorǁ_ellipsis__mutmut_1, 
        'xǁValidationErrorǁ_ellipsis__mutmut_2': xǁValidationErrorǁ_ellipsis__mutmut_2, 
        'xǁValidationErrorǁ_ellipsis__mutmut_3': xǁValidationErrorǁ_ellipsis__mutmut_3
    }
    
    def _ellipsis(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ_ellipsis__mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ_ellipsis__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _ellipsis.__signature__ = _mutmut_signature(xǁValidationErrorǁ_ellipsis__mutmut_orig)
    xǁValidationErrorǁ_ellipsis__mutmut_orig.__name__ = 'xǁValidationErrorǁ_ellipsis'

    def xǁValidationErrorǁ_truncate__mutmut_orig(self, template: str, **kwargs):
        return template.format(**{k: self._ellipsis(str(v)) for k, v in kwargs.items()})

    def xǁValidationErrorǁ_truncate__mutmut_1(self, template: str, **kwargs):
        return template.format(**{k: self._ellipsis(None) for k, v in kwargs.items()})

    def xǁValidationErrorǁ_truncate__mutmut_2(self, template: str, **kwargs):
        return template.format(**{k: self._ellipsis(str(None)) for k, v in kwargs.items()})
    
    xǁValidationErrorǁ_truncate__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ_truncate__mutmut_1': xǁValidationErrorǁ_truncate__mutmut_1, 
        'xǁValidationErrorǁ_truncate__mutmut_2': xǁValidationErrorǁ_truncate__mutmut_2
    }
    
    def _truncate(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ_truncate__mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ_truncate__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _truncate.__signature__ = _mutmut_signature(xǁValidationErrorǁ_truncate__mutmut_orig)
    xǁValidationErrorǁ_truncate__mutmut_orig.__name__ = 'xǁValidationErrorǁ_truncate'

    def xǁValidationErrorǁ_get_schema_name__mutmut_orig(self) -> str:
        if not self.schema:
            return ""
        if isinstance(self.schema, str):
            return f"({self.schema})"
        return f"({self.schema.__name__})"  # type: ignore[attr-defined]

    def xǁValidationErrorǁ_get_schema_name__mutmut_1(self) -> str:
        if self.schema:
            return ""
        if isinstance(self.schema, str):
            return f"({self.schema})"
        return f"({self.schema.__name__})"  # type: ignore[attr-defined]

    def xǁValidationErrorǁ_get_schema_name__mutmut_2(self) -> str:
        if not self.schema:
            return "XXXX"
        if isinstance(self.schema, str):
            return f"({self.schema})"
        return f"({self.schema.__name__})"  # type: ignore[attr-defined]
    
    xǁValidationErrorǁ_get_schema_name__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ_get_schema_name__mutmut_1': xǁValidationErrorǁ_get_schema_name__mutmut_1, 
        'xǁValidationErrorǁ_get_schema_name__mutmut_2': xǁValidationErrorǁ_get_schema_name__mutmut_2
    }
    
    def _get_schema_name(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ_get_schema_name__mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ_get_schema_name__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _get_schema_name.__signature__ = _mutmut_signature(xǁValidationErrorǁ_get_schema_name__mutmut_orig)
    xǁValidationErrorǁ_get_schema_name__mutmut_orig.__name__ = 'xǁValidationErrorǁ_get_schema_name'

    def xǁValidationErrorǁ__str____mutmut_orig(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_1(self):
        cls = None
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_2(self):
        cls = self.__class__
        ret = None
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_3(self):
        cls = self.__class__
        ret = []
        seen = None

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_4(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(None)

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_5(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(None, indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_6(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", None))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_7(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_8(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", ))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_9(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = None

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_10(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "XX  XX" * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_11(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " / level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_12(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error not in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_13(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(None, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_14(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, None)
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_15(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append("...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_16(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, )
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_17(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "XX...XX")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_18(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(None)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_19(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_20(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(None, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_21(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, None)
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_22(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_23(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, )
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_24(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(None, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_25(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, None)
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_26(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_27(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, )
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_28(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(None, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_29(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, None)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_30(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_31(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, )

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_32(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level - 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_33(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 2, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_34(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = None
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_35(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_36(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(None, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_37(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, None)
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_38(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append("Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_39(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, )
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_40(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "XXContext:XX")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_41(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_42(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "CONTEXT:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_43(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(None, context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_44(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", None)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_45(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_46(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", )
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_47(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(None, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_48(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, None)
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_49(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_50(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, )
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_51(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(None, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_52(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, None)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_53(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_54(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, )

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_55(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level - 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_56(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 2, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_57(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append(None, f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_58(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", None)
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_59(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append(f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_60(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", )
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_61(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("XXXX", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_62(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(None, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_63(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, None)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_64(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_65(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, )

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_66(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(2, self)

        return "\n".join(ret)

    def xǁValidationErrorǁ__str____mutmut_67(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\n".join(None)

    def xǁValidationErrorǁ__str____mutmut_68(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "XX\nXX".join(ret)

    def xǁValidationErrorǁ__str____mutmut_69(self):
        cls = self.__class__
        ret = []
        seen = set()

        def append(indentation, error):
            if error:
                ret.append(indent(f"{error}", indentation))

        def add(level, error):
            indentation = "  " * level

            if error in seen:
                append(indentation, "...")
                return
            seen.add(error)

            for err in error.errors:
                if not isinstance(err, cls):
                    append(indentation, f"{err}")
                else:
                    append(indentation, f"{err.__class__.__name__}{err._get_schema_name()}:")
                    add(level + 1, err)

            context = error.__cause__
            if context:
                if not isinstance(context, cls):
                    append(indentation, "Context:")
                    append(f"{indentation}  ", context)
                else:
                    append(indentation, f"Context{context._get_schema_name()}:")
                    add(level + 1, context)

        append("", f"{cls.__name__}{self._get_schema_name()}:")
        add(1, self)

        return "\N".join(ret)
    
    xǁValidationErrorǁ__str____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁValidationErrorǁ__str____mutmut_1': xǁValidationErrorǁ__str____mutmut_1, 
        'xǁValidationErrorǁ__str____mutmut_2': xǁValidationErrorǁ__str____mutmut_2, 
        'xǁValidationErrorǁ__str____mutmut_3': xǁValidationErrorǁ__str____mutmut_3, 
        'xǁValidationErrorǁ__str____mutmut_4': xǁValidationErrorǁ__str____mutmut_4, 
        'xǁValidationErrorǁ__str____mutmut_5': xǁValidationErrorǁ__str____mutmut_5, 
        'xǁValidationErrorǁ__str____mutmut_6': xǁValidationErrorǁ__str____mutmut_6, 
        'xǁValidationErrorǁ__str____mutmut_7': xǁValidationErrorǁ__str____mutmut_7, 
        'xǁValidationErrorǁ__str____mutmut_8': xǁValidationErrorǁ__str____mutmut_8, 
        'xǁValidationErrorǁ__str____mutmut_9': xǁValidationErrorǁ__str____mutmut_9, 
        'xǁValidationErrorǁ__str____mutmut_10': xǁValidationErrorǁ__str____mutmut_10, 
        'xǁValidationErrorǁ__str____mutmut_11': xǁValidationErrorǁ__str____mutmut_11, 
        'xǁValidationErrorǁ__str____mutmut_12': xǁValidationErrorǁ__str____mutmut_12, 
        'xǁValidationErrorǁ__str____mutmut_13': xǁValidationErrorǁ__str____mutmut_13, 
        'xǁValidationErrorǁ__str____mutmut_14': xǁValidationErrorǁ__str____mutmut_14, 
        'xǁValidationErrorǁ__str____mutmut_15': xǁValidationErrorǁ__str____mutmut_15, 
        'xǁValidationErrorǁ__str____mutmut_16': xǁValidationErrorǁ__str____mutmut_16, 
        'xǁValidationErrorǁ__str____mutmut_17': xǁValidationErrorǁ__str____mutmut_17, 
        'xǁValidationErrorǁ__str____mutmut_18': xǁValidationErrorǁ__str____mutmut_18, 
        'xǁValidationErrorǁ__str____mutmut_19': xǁValidationErrorǁ__str____mutmut_19, 
        'xǁValidationErrorǁ__str____mutmut_20': xǁValidationErrorǁ__str____mutmut_20, 
        'xǁValidationErrorǁ__str____mutmut_21': xǁValidationErrorǁ__str____mutmut_21, 
        'xǁValidationErrorǁ__str____mutmut_22': xǁValidationErrorǁ__str____mutmut_22, 
        'xǁValidationErrorǁ__str____mutmut_23': xǁValidationErrorǁ__str____mutmut_23, 
        'xǁValidationErrorǁ__str____mutmut_24': xǁValidationErrorǁ__str____mutmut_24, 
        'xǁValidationErrorǁ__str____mutmut_25': xǁValidationErrorǁ__str____mutmut_25, 
        'xǁValidationErrorǁ__str____mutmut_26': xǁValidationErrorǁ__str____mutmut_26, 
        'xǁValidationErrorǁ__str____mutmut_27': xǁValidationErrorǁ__str____mutmut_27, 
        'xǁValidationErrorǁ__str____mutmut_28': xǁValidationErrorǁ__str____mutmut_28, 
        'xǁValidationErrorǁ__str____mutmut_29': xǁValidationErrorǁ__str____mutmut_29, 
        'xǁValidationErrorǁ__str____mutmut_30': xǁValidationErrorǁ__str____mutmut_30, 
        'xǁValidationErrorǁ__str____mutmut_31': xǁValidationErrorǁ__str____mutmut_31, 
        'xǁValidationErrorǁ__str____mutmut_32': xǁValidationErrorǁ__str____mutmut_32, 
        'xǁValidationErrorǁ__str____mutmut_33': xǁValidationErrorǁ__str____mutmut_33, 
        'xǁValidationErrorǁ__str____mutmut_34': xǁValidationErrorǁ__str____mutmut_34, 
        'xǁValidationErrorǁ__str____mutmut_35': xǁValidationErrorǁ__str____mutmut_35, 
        'xǁValidationErrorǁ__str____mutmut_36': xǁValidationErrorǁ__str____mutmut_36, 
        'xǁValidationErrorǁ__str____mutmut_37': xǁValidationErrorǁ__str____mutmut_37, 
        'xǁValidationErrorǁ__str____mutmut_38': xǁValidationErrorǁ__str____mutmut_38, 
        'xǁValidationErrorǁ__str____mutmut_39': xǁValidationErrorǁ__str____mutmut_39, 
        'xǁValidationErrorǁ__str____mutmut_40': xǁValidationErrorǁ__str____mutmut_40, 
        'xǁValidationErrorǁ__str____mutmut_41': xǁValidationErrorǁ__str____mutmut_41, 
        'xǁValidationErrorǁ__str____mutmut_42': xǁValidationErrorǁ__str____mutmut_42, 
        'xǁValidationErrorǁ__str____mutmut_43': xǁValidationErrorǁ__str____mutmut_43, 
        'xǁValidationErrorǁ__str____mutmut_44': xǁValidationErrorǁ__str____mutmut_44, 
        'xǁValidationErrorǁ__str____mutmut_45': xǁValidationErrorǁ__str____mutmut_45, 
        'xǁValidationErrorǁ__str____mutmut_46': xǁValidationErrorǁ__str____mutmut_46, 
        'xǁValidationErrorǁ__str____mutmut_47': xǁValidationErrorǁ__str____mutmut_47, 
        'xǁValidationErrorǁ__str____mutmut_48': xǁValidationErrorǁ__str____mutmut_48, 
        'xǁValidationErrorǁ__str____mutmut_49': xǁValidationErrorǁ__str____mutmut_49, 
        'xǁValidationErrorǁ__str____mutmut_50': xǁValidationErrorǁ__str____mutmut_50, 
        'xǁValidationErrorǁ__str____mutmut_51': xǁValidationErrorǁ__str____mutmut_51, 
        'xǁValidationErrorǁ__str____mutmut_52': xǁValidationErrorǁ__str____mutmut_52, 
        'xǁValidationErrorǁ__str____mutmut_53': xǁValidationErrorǁ__str____mutmut_53, 
        'xǁValidationErrorǁ__str____mutmut_54': xǁValidationErrorǁ__str____mutmut_54, 
        'xǁValidationErrorǁ__str____mutmut_55': xǁValidationErrorǁ__str____mutmut_55, 
        'xǁValidationErrorǁ__str____mutmut_56': xǁValidationErrorǁ__str____mutmut_56, 
        'xǁValidationErrorǁ__str____mutmut_57': xǁValidationErrorǁ__str____mutmut_57, 
        'xǁValidationErrorǁ__str____mutmut_58': xǁValidationErrorǁ__str____mutmut_58, 
        'xǁValidationErrorǁ__str____mutmut_59': xǁValidationErrorǁ__str____mutmut_59, 
        'xǁValidationErrorǁ__str____mutmut_60': xǁValidationErrorǁ__str____mutmut_60, 
        'xǁValidationErrorǁ__str____mutmut_61': xǁValidationErrorǁ__str____mutmut_61, 
        'xǁValidationErrorǁ__str____mutmut_62': xǁValidationErrorǁ__str____mutmut_62, 
        'xǁValidationErrorǁ__str____mutmut_63': xǁValidationErrorǁ__str____mutmut_63, 
        'xǁValidationErrorǁ__str____mutmut_64': xǁValidationErrorǁ__str____mutmut_64, 
        'xǁValidationErrorǁ__str____mutmut_65': xǁValidationErrorǁ__str____mutmut_65, 
        'xǁValidationErrorǁ__str____mutmut_66': xǁValidationErrorǁ__str____mutmut_66, 
        'xǁValidationErrorǁ__str____mutmut_67': xǁValidationErrorǁ__str____mutmut_67, 
        'xǁValidationErrorǁ__str____mutmut_68': xǁValidationErrorǁ__str____mutmut_68, 
        'xǁValidationErrorǁ__str____mutmut_69': xǁValidationErrorǁ__str____mutmut_69
    }
    
    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁValidationErrorǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁValidationErrorǁ__str____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __str__.__signature__ = _mutmut_signature(xǁValidationErrorǁ__str____mutmut_orig)
    xǁValidationErrorǁ__str____mutmut_orig.__name__ = 'xǁValidationErrorǁ__str__'

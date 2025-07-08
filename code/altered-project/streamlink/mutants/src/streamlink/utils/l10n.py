from __future__ import annotations

import locale
import logging
from warnings import catch_warnings

from pycountry import countries, languages  # type: ignore[import]


DEFAULT_LANGUAGE = "en"
DEFAULT_COUNTRY = "US"
DEFAULT_LANGUAGE_CODE = f"{DEFAULT_LANGUAGE}_{DEFAULT_COUNTRY}"

log = logging.getLogger(__name__)
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


class Country:
    def xǁCountryǁ__init____mutmut_orig(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.numeric = numeric
        self.name = name
        self.official_name = official_name
    def xǁCountryǁ__init____mutmut_1(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = None
        self.alpha3 = alpha3
        self.numeric = numeric
        self.name = name
        self.official_name = official_name
    def xǁCountryǁ__init____mutmut_2(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = alpha2
        self.alpha3 = None
        self.numeric = numeric
        self.name = name
        self.official_name = official_name
    def xǁCountryǁ__init____mutmut_3(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.numeric = None
        self.name = name
        self.official_name = official_name
    def xǁCountryǁ__init____mutmut_4(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.numeric = numeric
        self.name = None
        self.official_name = official_name
    def xǁCountryǁ__init____mutmut_5(self, alpha2, alpha3, numeric, name, official_name=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.numeric = numeric
        self.name = name
        self.official_name = None
    
    xǁCountryǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCountryǁ__init____mutmut_1': xǁCountryǁ__init____mutmut_1, 
        'xǁCountryǁ__init____mutmut_2': xǁCountryǁ__init____mutmut_2, 
        'xǁCountryǁ__init____mutmut_3': xǁCountryǁ__init____mutmut_3, 
        'xǁCountryǁ__init____mutmut_4': xǁCountryǁ__init____mutmut_4, 
        'xǁCountryǁ__init____mutmut_5': xǁCountryǁ__init____mutmut_5
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCountryǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁCountryǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁCountryǁ__init____mutmut_orig)
    xǁCountryǁ__init____mutmut_orig.__name__ = 'xǁCountryǁ__init__'

    @classmethod
    def get(cls, country):
        try:
            c = countries.lookup(country)

            # changed in pycountry 23.12.11: a UserWarning is emitted when the official_name is missing
            with catch_warnings(record=True):
                official_name = getattr(c, "official_name", c.name)

            return Country(
                c.alpha_2,
                c.alpha_3,
                c.numeric,
                c.name,
                official_name=official_name,
            )
        except LookupError as err:
            raise LookupError(f"Invalid country code: {country}") from err

    def xǁCountryǁ__hash____mutmut_orig(self):
        return hash((self.alpha2, self.alpha3, self.numeric, self.name, self.official_name))

    def xǁCountryǁ__hash____mutmut_1(self):
        return hash(None)
    
    xǁCountryǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCountryǁ__hash____mutmut_1': xǁCountryǁ__hash____mutmut_1
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCountryǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁCountryǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁCountryǁ__hash____mutmut_orig)
    xǁCountryǁ__hash____mutmut_orig.__name__ = 'xǁCountryǁ__hash__'

    def xǁCountryǁ__eq____mutmut_orig(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_1(self, other):
        return (
            (self.alpha2 or self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_2(self, other):
        return (
            (self.alpha2 and self.alpha2 != other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_3(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2) and (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_4(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 or self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_5(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 != other.alpha3)
            or (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_6(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3) and (self.numeric and self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_7(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric or self.numeric == other.numeric)
        )

    def xǁCountryǁ__eq____mutmut_8(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.numeric and self.numeric != other.numeric)
        )
    
    xǁCountryǁ__eq____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCountryǁ__eq____mutmut_1': xǁCountryǁ__eq____mutmut_1, 
        'xǁCountryǁ__eq____mutmut_2': xǁCountryǁ__eq____mutmut_2, 
        'xǁCountryǁ__eq____mutmut_3': xǁCountryǁ__eq____mutmut_3, 
        'xǁCountryǁ__eq____mutmut_4': xǁCountryǁ__eq____mutmut_4, 
        'xǁCountryǁ__eq____mutmut_5': xǁCountryǁ__eq____mutmut_5, 
        'xǁCountryǁ__eq____mutmut_6': xǁCountryǁ__eq____mutmut_6, 
        'xǁCountryǁ__eq____mutmut_7': xǁCountryǁ__eq____mutmut_7, 
        'xǁCountryǁ__eq____mutmut_8': xǁCountryǁ__eq____mutmut_8
    }
    
    def __eq__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCountryǁ__eq____mutmut_orig"), object.__getattribute__(self, "xǁCountryǁ__eq____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __eq__.__signature__ = _mutmut_signature(xǁCountryǁ__eq____mutmut_orig)
    xǁCountryǁ__eq____mutmut_orig.__name__ = 'xǁCountryǁ__eq__'

    def xǁCountryǁ__str____mutmut_orig(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_1(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            None,
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_2(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            None,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_3(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            None,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_4(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            None,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_5(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            None,
        )

    def xǁCountryǁ__str____mutmut_6(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_7(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_8(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_9(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_10(self):
        return "Country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            )

    def xǁCountryǁ__str____mutmut_11(self):
        return "XXCountry({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})XX".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_12(self):
        return "country({0!r}, {1!r}, {2!r}, {3!r}, official_name={4!r})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )

    def xǁCountryǁ__str____mutmut_13(self):
        return "COUNTRY({0!R}, {1!R}, {2!R}, {3!R}, OFFICIAL_NAME={4!R})".format(
            self.alpha2,
            self.alpha3,
            self.numeric,
            self.name,
            self.official_name,
        )
    
    xǁCountryǁ__str____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁCountryǁ__str____mutmut_1': xǁCountryǁ__str____mutmut_1, 
        'xǁCountryǁ__str____mutmut_2': xǁCountryǁ__str____mutmut_2, 
        'xǁCountryǁ__str____mutmut_3': xǁCountryǁ__str____mutmut_3, 
        'xǁCountryǁ__str____mutmut_4': xǁCountryǁ__str____mutmut_4, 
        'xǁCountryǁ__str____mutmut_5': xǁCountryǁ__str____mutmut_5, 
        'xǁCountryǁ__str____mutmut_6': xǁCountryǁ__str____mutmut_6, 
        'xǁCountryǁ__str____mutmut_7': xǁCountryǁ__str____mutmut_7, 
        'xǁCountryǁ__str____mutmut_8': xǁCountryǁ__str____mutmut_8, 
        'xǁCountryǁ__str____mutmut_9': xǁCountryǁ__str____mutmut_9, 
        'xǁCountryǁ__str____mutmut_10': xǁCountryǁ__str____mutmut_10, 
        'xǁCountryǁ__str____mutmut_11': xǁCountryǁ__str____mutmut_11, 
        'xǁCountryǁ__str____mutmut_12': xǁCountryǁ__str____mutmut_12, 
        'xǁCountryǁ__str____mutmut_13': xǁCountryǁ__str____mutmut_13
    }
    
    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁCountryǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁCountryǁ__str____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __str__.__signature__ = _mutmut_signature(xǁCountryǁ__str____mutmut_orig)
    xǁCountryǁ__str____mutmut_orig.__name__ = 'xǁCountryǁ__str__'


class Language:
    def xǁLanguageǁ__init____mutmut_orig(self, alpha2, alpha3, name, bibliographic=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.name = name
        self.bibliographic = bibliographic
    def xǁLanguageǁ__init____mutmut_1(self, alpha2, alpha3, name, bibliographic=None):
        self.alpha2 = None
        self.alpha3 = alpha3
        self.name = name
        self.bibliographic = bibliographic
    def xǁLanguageǁ__init____mutmut_2(self, alpha2, alpha3, name, bibliographic=None):
        self.alpha2 = alpha2
        self.alpha3 = None
        self.name = name
        self.bibliographic = bibliographic
    def xǁLanguageǁ__init____mutmut_3(self, alpha2, alpha3, name, bibliographic=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.name = None
        self.bibliographic = bibliographic
    def xǁLanguageǁ__init____mutmut_4(self, alpha2, alpha3, name, bibliographic=None):
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.name = name
        self.bibliographic = None
    
    xǁLanguageǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLanguageǁ__init____mutmut_1': xǁLanguageǁ__init____mutmut_1, 
        'xǁLanguageǁ__init____mutmut_2': xǁLanguageǁ__init____mutmut_2, 
        'xǁLanguageǁ__init____mutmut_3': xǁLanguageǁ__init____mutmut_3, 
        'xǁLanguageǁ__init____mutmut_4': xǁLanguageǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLanguageǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLanguageǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁLanguageǁ__init____mutmut_orig)
    xǁLanguageǁ__init____mutmut_orig.__name__ = 'xǁLanguageǁ__init__'

    @classmethod
    def get(cls, language):
        try:
            lang = (
                languages.get(alpha_2=language)
                or languages.get(alpha_3=language)
                or languages.get(bibliographic=language)
                or languages.get(name=language)
            )
            if not lang:
                raise KeyError(language)
            return Language(
                # some languages don't have an alpha_2 code
                getattr(lang, "alpha_2", ""),
                lang.alpha_3,
                lang.name,
                getattr(lang, "bibliographic", ""),
            )
        except LookupError as err:
            raise LookupError(f"Invalid language code: {language}") from err

    def xǁLanguageǁ__hash____mutmut_orig(self):
        return hash((self.alpha2, self.alpha3, self.name, self.bibliographic))

    def xǁLanguageǁ__hash____mutmut_1(self):
        return hash(None)
    
    xǁLanguageǁ__hash____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLanguageǁ__hash____mutmut_1': xǁLanguageǁ__hash____mutmut_1
    }
    
    def __hash__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLanguageǁ__hash____mutmut_orig"), object.__getattribute__(self, "xǁLanguageǁ__hash____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __hash__.__signature__ = _mutmut_signature(xǁLanguageǁ__hash____mutmut_orig)
    xǁLanguageǁ__hash____mutmut_orig.__name__ = 'xǁLanguageǁ__hash__'

    def xǁLanguageǁ__eq____mutmut_orig(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_1(self, other):
        return (
            (self.alpha2 or self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_2(self, other):
        return (
            (self.alpha2 and self.alpha2 != other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_3(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2) and (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_4(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 or self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_5(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 != other.alpha3)
            or (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_6(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3) and (self.bibliographic and self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_7(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic or self.bibliographic == other.bibliographic)
        )

    def xǁLanguageǁ__eq____mutmut_8(self, other):
        return (
            (self.alpha2 and self.alpha2 == other.alpha2)
            or (self.alpha3 and self.alpha3 == other.alpha3)
            or (self.bibliographic and self.bibliographic != other.bibliographic)
        )
    
    xǁLanguageǁ__eq____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLanguageǁ__eq____mutmut_1': xǁLanguageǁ__eq____mutmut_1, 
        'xǁLanguageǁ__eq____mutmut_2': xǁLanguageǁ__eq____mutmut_2, 
        'xǁLanguageǁ__eq____mutmut_3': xǁLanguageǁ__eq____mutmut_3, 
        'xǁLanguageǁ__eq____mutmut_4': xǁLanguageǁ__eq____mutmut_4, 
        'xǁLanguageǁ__eq____mutmut_5': xǁLanguageǁ__eq____mutmut_5, 
        'xǁLanguageǁ__eq____mutmut_6': xǁLanguageǁ__eq____mutmut_6, 
        'xǁLanguageǁ__eq____mutmut_7': xǁLanguageǁ__eq____mutmut_7, 
        'xǁLanguageǁ__eq____mutmut_8': xǁLanguageǁ__eq____mutmut_8
    }
    
    def __eq__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLanguageǁ__eq____mutmut_orig"), object.__getattribute__(self, "xǁLanguageǁ__eq____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __eq__.__signature__ = _mutmut_signature(xǁLanguageǁ__eq____mutmut_orig)
    xǁLanguageǁ__eq____mutmut_orig.__name__ = 'xǁLanguageǁ__eq__'

    def xǁLanguageǁ__str____mutmut_orig(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_1(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            None,
            self.alpha3,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_2(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            None,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_3(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            None,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_4(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            None,
        )

    def xǁLanguageǁ__str____mutmut_5(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha3,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_6(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_7(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_8(self):
        return "Language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            )

    def xǁLanguageǁ__str____mutmut_9(self):
        return "XXLanguage({0!r}, {1!r}, {2!r}, bibliographic={3!r})XX".format(
            self.alpha2,
            self.alpha3,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_10(self):
        return "language({0!r}, {1!r}, {2!r}, bibliographic={3!r})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            self.bibliographic,
        )

    def xǁLanguageǁ__str____mutmut_11(self):
        return "LANGUAGE({0!R}, {1!R}, {2!R}, BIBLIOGRAPHIC={3!R})".format(
            self.alpha2,
            self.alpha3,
            self.name,
            self.bibliographic,
        )
    
    xǁLanguageǁ__str____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLanguageǁ__str____mutmut_1': xǁLanguageǁ__str____mutmut_1, 
        'xǁLanguageǁ__str____mutmut_2': xǁLanguageǁ__str____mutmut_2, 
        'xǁLanguageǁ__str____mutmut_3': xǁLanguageǁ__str____mutmut_3, 
        'xǁLanguageǁ__str____mutmut_4': xǁLanguageǁ__str____mutmut_4, 
        'xǁLanguageǁ__str____mutmut_5': xǁLanguageǁ__str____mutmut_5, 
        'xǁLanguageǁ__str____mutmut_6': xǁLanguageǁ__str____mutmut_6, 
        'xǁLanguageǁ__str____mutmut_7': xǁLanguageǁ__str____mutmut_7, 
        'xǁLanguageǁ__str____mutmut_8': xǁLanguageǁ__str____mutmut_8, 
        'xǁLanguageǁ__str____mutmut_9': xǁLanguageǁ__str____mutmut_9, 
        'xǁLanguageǁ__str____mutmut_10': xǁLanguageǁ__str____mutmut_10, 
        'xǁLanguageǁ__str____mutmut_11': xǁLanguageǁ__str____mutmut_11
    }
    
    def __str__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLanguageǁ__str____mutmut_orig"), object.__getattribute__(self, "xǁLanguageǁ__str____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __str__.__signature__ = _mutmut_signature(xǁLanguageǁ__str____mutmut_orig)
    xǁLanguageǁ__str____mutmut_orig.__name__ = 'xǁLanguageǁ__str__'


class Localization:
    def xǁLocalizationǁ__init____mutmut_orig(self, language_code=None):
        self._language_code = None
        self.country = None
        self.language = None
        self.explicit = bool(language_code)
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_1(self, language_code=None):
        self._language_code = ""
        self.country = None
        self.language = None
        self.explicit = bool(language_code)
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_2(self, language_code=None):
        self._language_code = None
        self.country = ""
        self.language = None
        self.explicit = bool(language_code)
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_3(self, language_code=None):
        self._language_code = None
        self.country = None
        self.language = ""
        self.explicit = bool(language_code)
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_4(self, language_code=None):
        self._language_code = None
        self.country = None
        self.language = None
        self.explicit = None
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_5(self, language_code=None):
        self._language_code = None
        self.country = None
        self.language = None
        self.explicit = bool(None)
        self._set_language_code(language_code)
    def xǁLocalizationǁ__init____mutmut_6(self, language_code=None):
        self._language_code = None
        self.country = None
        self.language = None
        self.explicit = bool(language_code)
        self._set_language_code(None)
    
    xǁLocalizationǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocalizationǁ__init____mutmut_1': xǁLocalizationǁ__init____mutmut_1, 
        'xǁLocalizationǁ__init____mutmut_2': xǁLocalizationǁ__init____mutmut_2, 
        'xǁLocalizationǁ__init____mutmut_3': xǁLocalizationǁ__init____mutmut_3, 
        'xǁLocalizationǁ__init____mutmut_4': xǁLocalizationǁ__init____mutmut_4, 
        'xǁLocalizationǁ__init____mutmut_5': xǁLocalizationǁ__init____mutmut_5, 
        'xǁLocalizationǁ__init____mutmut_6': xǁLocalizationǁ__init____mutmut_6
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocalizationǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁLocalizationǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁLocalizationǁ__init____mutmut_orig)
    xǁLocalizationǁ__init____mutmut_orig.__name__ = 'xǁLocalizationǁ__init__'

    @property
    def language_code(self):
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        self._set_language_code(language_code)

    def xǁLocalizationǁ_parse_locale_code__mutmut_orig(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_1(self, language_code):
        parts = None
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_2(self, language_code):
        parts = language_code.split(None, 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_3(self, language_code):
        parts = language_code.split("_", None)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_4(self, language_code):
        parts = language_code.split(1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_5(self, language_code):
        parts = language_code.split("_", )
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_6(self, language_code):
        parts = language_code.rsplit("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_7(self, language_code):
        parts = language_code.split("XX_XX", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_8(self, language_code):
        parts = language_code.split("_", 2)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_9(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) == 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_10(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 3 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_11(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 and len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_12(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) == 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_13(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 3 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_14(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 and len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_15(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) == 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_16(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 3:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_17(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(None)
        return self.get_language(parts[0]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_18(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(None), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_19(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[1]), self.get_country(parts[1])

    def xǁLocalizationǁ_parse_locale_code__mutmut_20(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(None)

    def xǁLocalizationǁ_parse_locale_code__mutmut_21(self, language_code):
        parts = language_code.split("_", 1)
        if len(parts) != 2 or len(parts[0]) != 2 or len(parts[1]) != 2:
            raise LookupError(f"Invalid language code: {language_code}")
        return self.get_language(parts[0]), self.get_country(parts[2])
    
    xǁLocalizationǁ_parse_locale_code__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocalizationǁ_parse_locale_code__mutmut_1': xǁLocalizationǁ_parse_locale_code__mutmut_1, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_2': xǁLocalizationǁ_parse_locale_code__mutmut_2, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_3': xǁLocalizationǁ_parse_locale_code__mutmut_3, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_4': xǁLocalizationǁ_parse_locale_code__mutmut_4, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_5': xǁLocalizationǁ_parse_locale_code__mutmut_5, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_6': xǁLocalizationǁ_parse_locale_code__mutmut_6, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_7': xǁLocalizationǁ_parse_locale_code__mutmut_7, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_8': xǁLocalizationǁ_parse_locale_code__mutmut_8, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_9': xǁLocalizationǁ_parse_locale_code__mutmut_9, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_10': xǁLocalizationǁ_parse_locale_code__mutmut_10, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_11': xǁLocalizationǁ_parse_locale_code__mutmut_11, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_12': xǁLocalizationǁ_parse_locale_code__mutmut_12, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_13': xǁLocalizationǁ_parse_locale_code__mutmut_13, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_14': xǁLocalizationǁ_parse_locale_code__mutmut_14, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_15': xǁLocalizationǁ_parse_locale_code__mutmut_15, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_16': xǁLocalizationǁ_parse_locale_code__mutmut_16, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_17': xǁLocalizationǁ_parse_locale_code__mutmut_17, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_18': xǁLocalizationǁ_parse_locale_code__mutmut_18, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_19': xǁLocalizationǁ_parse_locale_code__mutmut_19, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_20': xǁLocalizationǁ_parse_locale_code__mutmut_20, 
        'xǁLocalizationǁ_parse_locale_code__mutmut_21': xǁLocalizationǁ_parse_locale_code__mutmut_21
    }
    
    def _parse_locale_code(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocalizationǁ_parse_locale_code__mutmut_orig"), object.__getattribute__(self, "xǁLocalizationǁ_parse_locale_code__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _parse_locale_code.__signature__ = _mutmut_signature(xǁLocalizationǁ_parse_locale_code__mutmut_orig)
    xǁLocalizationǁ_parse_locale_code__mutmut_orig.__name__ = 'xǁLocalizationǁ_parse_locale_code'

    def xǁLocalizationǁ_set_language_code__mutmut_orig(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_1(self, language_code):
        is_system_locale = None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_2(self, language_code):
        is_system_locale = language_code is not None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_3(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = None
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_4(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = ""
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_5(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is not None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_6(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None and language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_7(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code != "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_8(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "XXCXX":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_9(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "c":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_10(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = None

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_11(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = None
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_12(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(None)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_13(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = None
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_14(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_15(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = None
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_16(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(None)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_17(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = None
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_18(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(None)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_19(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = None
        log.debug(f"Language code: {self._language_code}")

    def xǁLocalizationǁ_set_language_code__mutmut_20(self, language_code):
        is_system_locale = language_code is None
        if is_system_locale:
            try:
                language_code, _ = locale.getlocale()
            except ValueError:
                language_code = None
            if language_code is None or language_code == "C":
                # cannot be determined
                language_code = DEFAULT_LANGUAGE_CODE

        try:
            self.language, self.country = self._parse_locale_code(language_code)
            self._language_code = language_code
        except LookupError:
            if not is_system_locale:
                raise
            # If the system locale returns an invalid code, use the default
            self.language = self.get_language(DEFAULT_LANGUAGE)
            self.country = self.get_country(DEFAULT_COUNTRY)
            self._language_code = DEFAULT_LANGUAGE_CODE
        log.debug(None)
    
    xǁLocalizationǁ_set_language_code__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocalizationǁ_set_language_code__mutmut_1': xǁLocalizationǁ_set_language_code__mutmut_1, 
        'xǁLocalizationǁ_set_language_code__mutmut_2': xǁLocalizationǁ_set_language_code__mutmut_2, 
        'xǁLocalizationǁ_set_language_code__mutmut_3': xǁLocalizationǁ_set_language_code__mutmut_3, 
        'xǁLocalizationǁ_set_language_code__mutmut_4': xǁLocalizationǁ_set_language_code__mutmut_4, 
        'xǁLocalizationǁ_set_language_code__mutmut_5': xǁLocalizationǁ_set_language_code__mutmut_5, 
        'xǁLocalizationǁ_set_language_code__mutmut_6': xǁLocalizationǁ_set_language_code__mutmut_6, 
        'xǁLocalizationǁ_set_language_code__mutmut_7': xǁLocalizationǁ_set_language_code__mutmut_7, 
        'xǁLocalizationǁ_set_language_code__mutmut_8': xǁLocalizationǁ_set_language_code__mutmut_8, 
        'xǁLocalizationǁ_set_language_code__mutmut_9': xǁLocalizationǁ_set_language_code__mutmut_9, 
        'xǁLocalizationǁ_set_language_code__mutmut_10': xǁLocalizationǁ_set_language_code__mutmut_10, 
        'xǁLocalizationǁ_set_language_code__mutmut_11': xǁLocalizationǁ_set_language_code__mutmut_11, 
        'xǁLocalizationǁ_set_language_code__mutmut_12': xǁLocalizationǁ_set_language_code__mutmut_12, 
        'xǁLocalizationǁ_set_language_code__mutmut_13': xǁLocalizationǁ_set_language_code__mutmut_13, 
        'xǁLocalizationǁ_set_language_code__mutmut_14': xǁLocalizationǁ_set_language_code__mutmut_14, 
        'xǁLocalizationǁ_set_language_code__mutmut_15': xǁLocalizationǁ_set_language_code__mutmut_15, 
        'xǁLocalizationǁ_set_language_code__mutmut_16': xǁLocalizationǁ_set_language_code__mutmut_16, 
        'xǁLocalizationǁ_set_language_code__mutmut_17': xǁLocalizationǁ_set_language_code__mutmut_17, 
        'xǁLocalizationǁ_set_language_code__mutmut_18': xǁLocalizationǁ_set_language_code__mutmut_18, 
        'xǁLocalizationǁ_set_language_code__mutmut_19': xǁLocalizationǁ_set_language_code__mutmut_19, 
        'xǁLocalizationǁ_set_language_code__mutmut_20': xǁLocalizationǁ_set_language_code__mutmut_20
    }
    
    def _set_language_code(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocalizationǁ_set_language_code__mutmut_orig"), object.__getattribute__(self, "xǁLocalizationǁ_set_language_code__mutmut_mutants"), args, kwargs, self)
        return result 
    
    _set_language_code.__signature__ = _mutmut_signature(xǁLocalizationǁ_set_language_code__mutmut_orig)
    xǁLocalizationǁ_set_language_code__mutmut_orig.__name__ = 'xǁLocalizationǁ_set_language_code'

    def xǁLocalizationǁequivalent__mutmut_orig(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_1(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_2(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language and isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_3(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) or self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_4(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language != language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_5(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language and self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_6(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language != self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_7(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(None)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_8(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                ) or (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_9(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_10(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country and isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_11(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) or self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_12(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country != country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_13(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country and self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_14(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country != self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_15(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(None)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return False

    def xǁLocalizationǁequivalent__mutmut_16(
        self,
        language: Language | str | None = None,
        country: Country | str | None = None,
    ) -> bool:
        try:
            return (
                (
                    not language
                    or isinstance(language, Language) and self.language == language
                    or self.language == self.get_language(language)
                )
                and (
                    not country
                    or isinstance(country, Country) and self.country == country
                    or self.country == self.get_country(country)
                )
            )  # fmt: skip
        except LookupError:
            # if an unknown language/country code is given, they cannot be equivalent
            return True
    
    xǁLocalizationǁequivalent__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁLocalizationǁequivalent__mutmut_1': xǁLocalizationǁequivalent__mutmut_1, 
        'xǁLocalizationǁequivalent__mutmut_2': xǁLocalizationǁequivalent__mutmut_2, 
        'xǁLocalizationǁequivalent__mutmut_3': xǁLocalizationǁequivalent__mutmut_3, 
        'xǁLocalizationǁequivalent__mutmut_4': xǁLocalizationǁequivalent__mutmut_4, 
        'xǁLocalizationǁequivalent__mutmut_5': xǁLocalizationǁequivalent__mutmut_5, 
        'xǁLocalizationǁequivalent__mutmut_6': xǁLocalizationǁequivalent__mutmut_6, 
        'xǁLocalizationǁequivalent__mutmut_7': xǁLocalizationǁequivalent__mutmut_7, 
        'xǁLocalizationǁequivalent__mutmut_8': xǁLocalizationǁequivalent__mutmut_8, 
        'xǁLocalizationǁequivalent__mutmut_9': xǁLocalizationǁequivalent__mutmut_9, 
        'xǁLocalizationǁequivalent__mutmut_10': xǁLocalizationǁequivalent__mutmut_10, 
        'xǁLocalizationǁequivalent__mutmut_11': xǁLocalizationǁequivalent__mutmut_11, 
        'xǁLocalizationǁequivalent__mutmut_12': xǁLocalizationǁequivalent__mutmut_12, 
        'xǁLocalizationǁequivalent__mutmut_13': xǁLocalizationǁequivalent__mutmut_13, 
        'xǁLocalizationǁequivalent__mutmut_14': xǁLocalizationǁequivalent__mutmut_14, 
        'xǁLocalizationǁequivalent__mutmut_15': xǁLocalizationǁequivalent__mutmut_15, 
        'xǁLocalizationǁequivalent__mutmut_16': xǁLocalizationǁequivalent__mutmut_16
    }
    
    def equivalent(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁLocalizationǁequivalent__mutmut_orig"), object.__getattribute__(self, "xǁLocalizationǁequivalent__mutmut_mutants"), args, kwargs, self)
        return result 
    
    equivalent.__signature__ = _mutmut_signature(xǁLocalizationǁequivalent__mutmut_orig)
    xǁLocalizationǁequivalent__mutmut_orig.__name__ = 'xǁLocalizationǁequivalent'

    @classmethod
    def get_country(cls, country):
        return Country.get(country)

    @classmethod
    def get_language(cls, language):
        return Language.get(language)

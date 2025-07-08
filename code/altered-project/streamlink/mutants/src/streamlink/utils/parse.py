import json
import re
from urllib.parse import parse_qsl

from lxml.etree import HTML, XML

from streamlink.compat import detect_encoding
from streamlink.exceptions import PluginError
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


def x__parse__mutmut_orig(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_1(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = None
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_2(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(None, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_3(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(*args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_4(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_5(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, )
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_6(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = None
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_7(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(None)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_8(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) >= 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_9(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 36:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_10(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = None

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_11(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:36]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_12(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(None)  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=exception)

    return parsed


def x__parse__mutmut_13(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = None

    return parsed


def x__parse__mutmut_14(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(None, name=name, exception=exception)

    return parsed


def x__parse__mutmut_15(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=None, exception=exception)

    return parsed


def x__parse__mutmut_16(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, exception=None)

    return parsed


def x__parse__mutmut_17(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(name=name, exception=exception)

    return parsed


def x__parse__mutmut_18(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, exception=exception)

    return parsed


def x__parse__mutmut_19(parser, data, name, exception, schema, *args, **kwargs):
    try:
        parsed = parser(data, *args, **kwargs)
    except Exception as err:
        snippet = repr(data)
        if len(snippet) > 35:
            snippet = f"{snippet[:35]} ..."

        raise exception(f"Unable to parse {name}: {err} ({snippet})")  # noqa: B904

    if schema:
        parsed = schema.validate(parsed, name=name, )

    return parsed

x__parse__mutmut_mutants : ClassVar[MutantDict] = {
'x__parse__mutmut_1': x__parse__mutmut_1, 
    'x__parse__mutmut_2': x__parse__mutmut_2, 
    'x__parse__mutmut_3': x__parse__mutmut_3, 
    'x__parse__mutmut_4': x__parse__mutmut_4, 
    'x__parse__mutmut_5': x__parse__mutmut_5, 
    'x__parse__mutmut_6': x__parse__mutmut_6, 
    'x__parse__mutmut_7': x__parse__mutmut_7, 
    'x__parse__mutmut_8': x__parse__mutmut_8, 
    'x__parse__mutmut_9': x__parse__mutmut_9, 
    'x__parse__mutmut_10': x__parse__mutmut_10, 
    'x__parse__mutmut_11': x__parse__mutmut_11, 
    'x__parse__mutmut_12': x__parse__mutmut_12, 
    'x__parse__mutmut_13': x__parse__mutmut_13, 
    'x__parse__mutmut_14': x__parse__mutmut_14, 
    'x__parse__mutmut_15': x__parse__mutmut_15, 
    'x__parse__mutmut_16': x__parse__mutmut_16, 
    'x__parse__mutmut_17': x__parse__mutmut_17, 
    'x__parse__mutmut_18': x__parse__mutmut_18, 
    'x__parse__mutmut_19': x__parse__mutmut_19
}

def _parse(*args, **kwargs):
    result = _mutmut_trampoline(x__parse__mutmut_orig, x__parse__mutmut_mutants, args, kwargs)
    return result 

_parse.__signature__ = _mutmut_signature(x__parse__mutmut_orig)
x__parse__mutmut_orig.__name__ = 'x__parse'


def x_parse_json__mutmut_orig(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_1(
    data,
    name="XXJSONXX",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_2(
    data,
    name="json",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_3(
    data,
    name="Json",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_4(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(None, data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_5(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, None, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_6(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, None, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_7(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, None, schema, *args, **kwargs)


def x_parse_json__mutmut_8(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, None, *args, **kwargs)


def x_parse_json__mutmut_9(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(data, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_10(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, name, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_11(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, exception, schema, *args, **kwargs)


def x_parse_json__mutmut_12(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, schema, *args, **kwargs)


def x_parse_json__mutmut_13(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, *args, **kwargs)


def x_parse_json__mutmut_14(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, **kwargs)


def x_parse_json__mutmut_15(
    data,
    name="JSON",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around json.loads.

    Provides these extra features:
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(json.loads, data, name, exception, schema, *args, )

x_parse_json__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_json__mutmut_1': x_parse_json__mutmut_1, 
    'x_parse_json__mutmut_2': x_parse_json__mutmut_2, 
    'x_parse_json__mutmut_3': x_parse_json__mutmut_3, 
    'x_parse_json__mutmut_4': x_parse_json__mutmut_4, 
    'x_parse_json__mutmut_5': x_parse_json__mutmut_5, 
    'x_parse_json__mutmut_6': x_parse_json__mutmut_6, 
    'x_parse_json__mutmut_7': x_parse_json__mutmut_7, 
    'x_parse_json__mutmut_8': x_parse_json__mutmut_8, 
    'x_parse_json__mutmut_9': x_parse_json__mutmut_9, 
    'x_parse_json__mutmut_10': x_parse_json__mutmut_10, 
    'x_parse_json__mutmut_11': x_parse_json__mutmut_11, 
    'x_parse_json__mutmut_12': x_parse_json__mutmut_12, 
    'x_parse_json__mutmut_13': x_parse_json__mutmut_13, 
    'x_parse_json__mutmut_14': x_parse_json__mutmut_14, 
    'x_parse_json__mutmut_15': x_parse_json__mutmut_15
}

def parse_json(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_json__mutmut_orig, x_parse_json__mutmut_mutants, args, kwargs)
    return result 

parse_json.__signature__ = _mutmut_signature(x_parse_json__mutmut_orig)
x_parse_json__mutmut_orig.__name__ = 'x_parse_json'


def x_parse_html__mutmut_orig(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_1(
    data,
    name="XXHTMLXX",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_2(
    data,
    name="html",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_3(
    data,
    name="Html",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_4(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = None
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_5(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data or data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_6(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].upper() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_7(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.rstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_8(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:6].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_9(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() != (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_10(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"XX<?xmlXX" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_11(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_12(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?XML" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_13(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_14(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "XX<?xmlXX"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_15(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?XML"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_16(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = None
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_17(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(None, data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_18(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", None, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_19(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, None)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_20(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_21(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_22(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, )
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_23(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"XX^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>XX", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_24(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?p<q>[\'\"])(?p<encoding>.+?)(?p=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_25(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\S*<\?XML\S.*?ENCODING=(?P<Q>[\'\"])(?P<ENCODING>.+?)(?P=Q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_26(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?p<q>[\'\"])(?p<encoding>.+?)(?p=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_27(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = None
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_28(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(None)["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_29(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["XXencodingXX"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_30(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["ENCODING"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_31(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["Encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_32(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["XXencodingXX"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_33(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["ENCODING"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_34(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["Encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_35(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = None
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_36(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(None)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_37(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["XXencodingXX"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_38(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["ENCODING"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_39(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["Encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_40(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = None

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_41(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(None)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_42(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["XXencodingXX"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_43(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["ENCODING"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_44(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["Encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_45(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = None

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_46(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(None)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_47(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = None

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_48(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(None, "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_49(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", None, data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_50(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", None)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_51(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub("", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_52(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_53(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", )

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_54(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"XX^\s*<\?xml.+?\?>XX", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_55(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_56(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\S*<\?XML.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_57(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_58(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "XXXX", data)

    return _parse(HTML, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_59(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(None, data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_60(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, None, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_61(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, None, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_62(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, None, schema, *args, **kwargs)


def x_parse_html__mutmut_63(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, None, *args, **kwargs)


def x_parse_html__mutmut_64(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(data, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_65(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, name, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_66(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, exception, schema, *args, **kwargs)


def x_parse_html__mutmut_67(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, schema, *args, **kwargs)


def x_parse_html__mutmut_68(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, *args, **kwargs)


def x_parse_html__mutmut_69(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, **kwargs)


def x_parse_html__mutmut_70(
    data,
    name="HTML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.HTML with some extras.

    Provides these extra features:
     - Removes XML declarations of invalid XHTML5 documents
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    # strip XML text declarations from XHTML5 documents which were incorrectly defined as HTML5
    is_bytes = isinstance(data, bytes)
    if data and data.lstrip()[:5].lower() == (b"<?xml" if is_bytes else "<?xml"):
        if is_bytes:
            # get the document's encoding using the "encoding" attribute value of the XML text declaration
            match = re.match(rb"^\s*<\?xml\s.*?encoding=(?P<q>[\'\"])(?P<encoding>.+?)(?P=q).*?\?>", data, re.IGNORECASE)
            if match:
                encoding_value = detect_encoding(match["encoding"])["encoding"]
                encoding = match["encoding"].decode(encoding_value)
            else:
                # no "encoding" attribute: try to figure out encoding from the document's content
                encoding = detect_encoding(data)["encoding"]

            data = data.decode(encoding)

        data = re.sub(r"^\s*<\?xml.+?\?>", "", data)

    return _parse(HTML, data, name, exception, schema, *args, )

x_parse_html__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_html__mutmut_1': x_parse_html__mutmut_1, 
    'x_parse_html__mutmut_2': x_parse_html__mutmut_2, 
    'x_parse_html__mutmut_3': x_parse_html__mutmut_3, 
    'x_parse_html__mutmut_4': x_parse_html__mutmut_4, 
    'x_parse_html__mutmut_5': x_parse_html__mutmut_5, 
    'x_parse_html__mutmut_6': x_parse_html__mutmut_6, 
    'x_parse_html__mutmut_7': x_parse_html__mutmut_7, 
    'x_parse_html__mutmut_8': x_parse_html__mutmut_8, 
    'x_parse_html__mutmut_9': x_parse_html__mutmut_9, 
    'x_parse_html__mutmut_10': x_parse_html__mutmut_10, 
    'x_parse_html__mutmut_11': x_parse_html__mutmut_11, 
    'x_parse_html__mutmut_12': x_parse_html__mutmut_12, 
    'x_parse_html__mutmut_13': x_parse_html__mutmut_13, 
    'x_parse_html__mutmut_14': x_parse_html__mutmut_14, 
    'x_parse_html__mutmut_15': x_parse_html__mutmut_15, 
    'x_parse_html__mutmut_16': x_parse_html__mutmut_16, 
    'x_parse_html__mutmut_17': x_parse_html__mutmut_17, 
    'x_parse_html__mutmut_18': x_parse_html__mutmut_18, 
    'x_parse_html__mutmut_19': x_parse_html__mutmut_19, 
    'x_parse_html__mutmut_20': x_parse_html__mutmut_20, 
    'x_parse_html__mutmut_21': x_parse_html__mutmut_21, 
    'x_parse_html__mutmut_22': x_parse_html__mutmut_22, 
    'x_parse_html__mutmut_23': x_parse_html__mutmut_23, 
    'x_parse_html__mutmut_24': x_parse_html__mutmut_24, 
    'x_parse_html__mutmut_25': x_parse_html__mutmut_25, 
    'x_parse_html__mutmut_26': x_parse_html__mutmut_26, 
    'x_parse_html__mutmut_27': x_parse_html__mutmut_27, 
    'x_parse_html__mutmut_28': x_parse_html__mutmut_28, 
    'x_parse_html__mutmut_29': x_parse_html__mutmut_29, 
    'x_parse_html__mutmut_30': x_parse_html__mutmut_30, 
    'x_parse_html__mutmut_31': x_parse_html__mutmut_31, 
    'x_parse_html__mutmut_32': x_parse_html__mutmut_32, 
    'x_parse_html__mutmut_33': x_parse_html__mutmut_33, 
    'x_parse_html__mutmut_34': x_parse_html__mutmut_34, 
    'x_parse_html__mutmut_35': x_parse_html__mutmut_35, 
    'x_parse_html__mutmut_36': x_parse_html__mutmut_36, 
    'x_parse_html__mutmut_37': x_parse_html__mutmut_37, 
    'x_parse_html__mutmut_38': x_parse_html__mutmut_38, 
    'x_parse_html__mutmut_39': x_parse_html__mutmut_39, 
    'x_parse_html__mutmut_40': x_parse_html__mutmut_40, 
    'x_parse_html__mutmut_41': x_parse_html__mutmut_41, 
    'x_parse_html__mutmut_42': x_parse_html__mutmut_42, 
    'x_parse_html__mutmut_43': x_parse_html__mutmut_43, 
    'x_parse_html__mutmut_44': x_parse_html__mutmut_44, 
    'x_parse_html__mutmut_45': x_parse_html__mutmut_45, 
    'x_parse_html__mutmut_46': x_parse_html__mutmut_46, 
    'x_parse_html__mutmut_47': x_parse_html__mutmut_47, 
    'x_parse_html__mutmut_48': x_parse_html__mutmut_48, 
    'x_parse_html__mutmut_49': x_parse_html__mutmut_49, 
    'x_parse_html__mutmut_50': x_parse_html__mutmut_50, 
    'x_parse_html__mutmut_51': x_parse_html__mutmut_51, 
    'x_parse_html__mutmut_52': x_parse_html__mutmut_52, 
    'x_parse_html__mutmut_53': x_parse_html__mutmut_53, 
    'x_parse_html__mutmut_54': x_parse_html__mutmut_54, 
    'x_parse_html__mutmut_55': x_parse_html__mutmut_55, 
    'x_parse_html__mutmut_56': x_parse_html__mutmut_56, 
    'x_parse_html__mutmut_57': x_parse_html__mutmut_57, 
    'x_parse_html__mutmut_58': x_parse_html__mutmut_58, 
    'x_parse_html__mutmut_59': x_parse_html__mutmut_59, 
    'x_parse_html__mutmut_60': x_parse_html__mutmut_60, 
    'x_parse_html__mutmut_61': x_parse_html__mutmut_61, 
    'x_parse_html__mutmut_62': x_parse_html__mutmut_62, 
    'x_parse_html__mutmut_63': x_parse_html__mutmut_63, 
    'x_parse_html__mutmut_64': x_parse_html__mutmut_64, 
    'x_parse_html__mutmut_65': x_parse_html__mutmut_65, 
    'x_parse_html__mutmut_66': x_parse_html__mutmut_66, 
    'x_parse_html__mutmut_67': x_parse_html__mutmut_67, 
    'x_parse_html__mutmut_68': x_parse_html__mutmut_68, 
    'x_parse_html__mutmut_69': x_parse_html__mutmut_69, 
    'x_parse_html__mutmut_70': x_parse_html__mutmut_70
}

def parse_html(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_html__mutmut_orig, x_parse_html__mutmut_mutants, args, kwargs)
    return result 

parse_html.__signature__ = _mutmut_signature(x_parse_html__mutmut_orig)
x_parse_html__mutmut_orig.__name__ = 'x_parse_html'


def x_parse_xml__mutmut_orig(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_1(
    data,
    ignore_ns=True,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_2(
    data,
    ignore_ns=False,
    invalid_char_entities=True,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_3(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XXXMLXX",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_4(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="xml",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_5(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="Xml",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_6(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = None
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_7(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(None, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_8(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, None)
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_9(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes("utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_10(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, )
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_11(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "XXutf8XX")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_12(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "UTF8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_13(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "Utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_14(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = None
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_15(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(None, b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_16(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", None, data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_17(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", None)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_18(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_19(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_20(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", )
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_21(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"XX\s+xmlns=\"(.+?)\"XX", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_22(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_23(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\S+XMLNS=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_24(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_25(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"XXXX", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_26(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_27(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_28(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_29(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = None

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_30(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(None, b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_31(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", None, data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_32(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", None)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_33(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_34(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_35(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", )

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_36(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"XX&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)XX", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_37(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[xx][0-9a-fa-f]+)|[a-za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_38(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[XX][0-9A-FA-F]+)|[A-ZA-Z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_39(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[xx][0-9a-fa-f]+)|[a-za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_40(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"XX&amp;XX", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_41(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_42(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&AMP;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_43(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_44(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(None, data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_45(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, None, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_46(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, None, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_47(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, None, schema, *args, **kwargs)


def x_parse_xml__mutmut_48(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, None, *args, **kwargs)


def x_parse_xml__mutmut_49(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(data, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_50(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, name, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_51(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, exception, schema, *args, **kwargs)


def x_parse_xml__mutmut_52(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, schema, *args, **kwargs)


def x_parse_xml__mutmut_53(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, *args, **kwargs)


def x_parse_xml__mutmut_54(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, **kwargs)


def x_parse_xml__mutmut_55(
    data,
    ignore_ns=False,
    invalid_char_entities=False,
    name="XML",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Wrapper around lxml.etree.XML with some extras.

    Provides these extra features:
     - Handles incorrectly encoded XML
     - Allows stripping namespace information
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    if isinstance(data, str):
        data = bytes(data, "utf8")
    if ignore_ns:
        data = re.sub(rb"\s+xmlns=\"(.+?)\"", b"", data)
    if invalid_char_entities:
        data = re.sub(rb"&(?!(?:#(?:[0-9]+|[Xx][0-9A-Fa-f]+)|[A-Za-z0-9]+);)", b"&amp;", data)

    return _parse(XML, data, name, exception, schema, *args, )

x_parse_xml__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_xml__mutmut_1': x_parse_xml__mutmut_1, 
    'x_parse_xml__mutmut_2': x_parse_xml__mutmut_2, 
    'x_parse_xml__mutmut_3': x_parse_xml__mutmut_3, 
    'x_parse_xml__mutmut_4': x_parse_xml__mutmut_4, 
    'x_parse_xml__mutmut_5': x_parse_xml__mutmut_5, 
    'x_parse_xml__mutmut_6': x_parse_xml__mutmut_6, 
    'x_parse_xml__mutmut_7': x_parse_xml__mutmut_7, 
    'x_parse_xml__mutmut_8': x_parse_xml__mutmut_8, 
    'x_parse_xml__mutmut_9': x_parse_xml__mutmut_9, 
    'x_parse_xml__mutmut_10': x_parse_xml__mutmut_10, 
    'x_parse_xml__mutmut_11': x_parse_xml__mutmut_11, 
    'x_parse_xml__mutmut_12': x_parse_xml__mutmut_12, 
    'x_parse_xml__mutmut_13': x_parse_xml__mutmut_13, 
    'x_parse_xml__mutmut_14': x_parse_xml__mutmut_14, 
    'x_parse_xml__mutmut_15': x_parse_xml__mutmut_15, 
    'x_parse_xml__mutmut_16': x_parse_xml__mutmut_16, 
    'x_parse_xml__mutmut_17': x_parse_xml__mutmut_17, 
    'x_parse_xml__mutmut_18': x_parse_xml__mutmut_18, 
    'x_parse_xml__mutmut_19': x_parse_xml__mutmut_19, 
    'x_parse_xml__mutmut_20': x_parse_xml__mutmut_20, 
    'x_parse_xml__mutmut_21': x_parse_xml__mutmut_21, 
    'x_parse_xml__mutmut_22': x_parse_xml__mutmut_22, 
    'x_parse_xml__mutmut_23': x_parse_xml__mutmut_23, 
    'x_parse_xml__mutmut_24': x_parse_xml__mutmut_24, 
    'x_parse_xml__mutmut_25': x_parse_xml__mutmut_25, 
    'x_parse_xml__mutmut_26': x_parse_xml__mutmut_26, 
    'x_parse_xml__mutmut_27': x_parse_xml__mutmut_27, 
    'x_parse_xml__mutmut_28': x_parse_xml__mutmut_28, 
    'x_parse_xml__mutmut_29': x_parse_xml__mutmut_29, 
    'x_parse_xml__mutmut_30': x_parse_xml__mutmut_30, 
    'x_parse_xml__mutmut_31': x_parse_xml__mutmut_31, 
    'x_parse_xml__mutmut_32': x_parse_xml__mutmut_32, 
    'x_parse_xml__mutmut_33': x_parse_xml__mutmut_33, 
    'x_parse_xml__mutmut_34': x_parse_xml__mutmut_34, 
    'x_parse_xml__mutmut_35': x_parse_xml__mutmut_35, 
    'x_parse_xml__mutmut_36': x_parse_xml__mutmut_36, 
    'x_parse_xml__mutmut_37': x_parse_xml__mutmut_37, 
    'x_parse_xml__mutmut_38': x_parse_xml__mutmut_38, 
    'x_parse_xml__mutmut_39': x_parse_xml__mutmut_39, 
    'x_parse_xml__mutmut_40': x_parse_xml__mutmut_40, 
    'x_parse_xml__mutmut_41': x_parse_xml__mutmut_41, 
    'x_parse_xml__mutmut_42': x_parse_xml__mutmut_42, 
    'x_parse_xml__mutmut_43': x_parse_xml__mutmut_43, 
    'x_parse_xml__mutmut_44': x_parse_xml__mutmut_44, 
    'x_parse_xml__mutmut_45': x_parse_xml__mutmut_45, 
    'x_parse_xml__mutmut_46': x_parse_xml__mutmut_46, 
    'x_parse_xml__mutmut_47': x_parse_xml__mutmut_47, 
    'x_parse_xml__mutmut_48': x_parse_xml__mutmut_48, 
    'x_parse_xml__mutmut_49': x_parse_xml__mutmut_49, 
    'x_parse_xml__mutmut_50': x_parse_xml__mutmut_50, 
    'x_parse_xml__mutmut_51': x_parse_xml__mutmut_51, 
    'x_parse_xml__mutmut_52': x_parse_xml__mutmut_52, 
    'x_parse_xml__mutmut_53': x_parse_xml__mutmut_53, 
    'x_parse_xml__mutmut_54': x_parse_xml__mutmut_54, 
    'x_parse_xml__mutmut_55': x_parse_xml__mutmut_55
}

def parse_xml(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_xml__mutmut_orig, x_parse_xml__mutmut_mutants, args, kwargs)
    return result 

parse_xml.__signature__ = _mutmut_signature(x_parse_xml__mutmut_orig)
x_parse_xml__mutmut_orig.__name__ = 'x_parse_xml'


def x_parse_qsd__mutmut_orig(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_1(
    data,
    name="XXquery stringXX",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_2(
    data,
    name="QUERY STRING",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_3(
    data,
    name="Query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_4(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(None, data, name, exception, schema)


def x_parse_qsd__mutmut_5(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), None, name, exception, schema)


def x_parse_qsd__mutmut_6(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, None, exception, schema)


def x_parse_qsd__mutmut_7(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, None, schema)


def x_parse_qsd__mutmut_8(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, None)


def x_parse_qsd__mutmut_9(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(data, name, exception, schema)


def x_parse_qsd__mutmut_10(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), name, exception, schema)


def x_parse_qsd__mutmut_11(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, exception, schema)


def x_parse_qsd__mutmut_12(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, schema)


def x_parse_qsd__mutmut_13(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, **kwargs)), data, name, exception, )


def x_parse_qsd__mutmut_14(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: None, data, name, exception, schema)


def x_parse_qsd__mutmut_15(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(None), data, name, exception, schema)


def x_parse_qsd__mutmut_16(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(None, *args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_17(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(*args, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_18(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, **kwargs)), data, name, exception, schema)


def x_parse_qsd__mutmut_19(
    data,
    name="query string",
    exception=PluginError,
    schema=None,
    *args,
    **kwargs,
):
    """Parses a query string into a dict.

    Provides these extra features:
     - Unlike parse_qs and parse_qsl, duplicate keys are not preserved in favor of a simpler return value
     - Wraps errors in custom exception with a snippet of the data in the message
    """
    return _parse(lambda d: dict(parse_qsl(d, *args, )), data, name, exception, schema)

x_parse_qsd__mutmut_mutants : ClassVar[MutantDict] = {
'x_parse_qsd__mutmut_1': x_parse_qsd__mutmut_1, 
    'x_parse_qsd__mutmut_2': x_parse_qsd__mutmut_2, 
    'x_parse_qsd__mutmut_3': x_parse_qsd__mutmut_3, 
    'x_parse_qsd__mutmut_4': x_parse_qsd__mutmut_4, 
    'x_parse_qsd__mutmut_5': x_parse_qsd__mutmut_5, 
    'x_parse_qsd__mutmut_6': x_parse_qsd__mutmut_6, 
    'x_parse_qsd__mutmut_7': x_parse_qsd__mutmut_7, 
    'x_parse_qsd__mutmut_8': x_parse_qsd__mutmut_8, 
    'x_parse_qsd__mutmut_9': x_parse_qsd__mutmut_9, 
    'x_parse_qsd__mutmut_10': x_parse_qsd__mutmut_10, 
    'x_parse_qsd__mutmut_11': x_parse_qsd__mutmut_11, 
    'x_parse_qsd__mutmut_12': x_parse_qsd__mutmut_12, 
    'x_parse_qsd__mutmut_13': x_parse_qsd__mutmut_13, 
    'x_parse_qsd__mutmut_14': x_parse_qsd__mutmut_14, 
    'x_parse_qsd__mutmut_15': x_parse_qsd__mutmut_15, 
    'x_parse_qsd__mutmut_16': x_parse_qsd__mutmut_16, 
    'x_parse_qsd__mutmut_17': x_parse_qsd__mutmut_17, 
    'x_parse_qsd__mutmut_18': x_parse_qsd__mutmut_18, 
    'x_parse_qsd__mutmut_19': x_parse_qsd__mutmut_19
}

def parse_qsd(*args, **kwargs):
    result = _mutmut_trampoline(x_parse_qsd__mutmut_orig, x_parse_qsd__mutmut_mutants, args, kwargs)
    return result 

parse_qsd.__signature__ = _mutmut_signature(x_parse_qsd__mutmut_orig)
x_parse_qsd__mutmut_orig.__name__ = 'x_parse_qsd'

import pytest
from hypothesis import given, strategies as st
from streamlink.plugin.plugin import parse_params

@given(st.none() | st.text())
def test_parse_params_random(params):
    # parse_params should always return a dict, even for None or random strings
    result = parse_params(params)
    assert isinstance(result, dict)
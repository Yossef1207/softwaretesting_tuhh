import pytest
from requests import Request
from streamlink.packages.requests_file import FileAdapter
from hypothesis import given, settings, strategies as st
import string

# Generate clearly invalid hostnames (no chance of accidental acceptance)
invalid_hostname_strategy = st.text(
    alphabet=string.ascii_letters + string.digits,
    min_size=1,
    max_size=10
)#.filter(lambda h: h not in {"localhost", ".", "..", "-"})

@given(host=invalid_hostname_strategy) #@settings(max_examples=50)
def test_fileadapter_reject_invalid_host(host):
    url = f"file://{host}/dummy.txt"
    request = Request("GET", url).prepare()
    adapter = FileAdapter()

    with pytest.raises(ValueError):
        adapter.send(request)

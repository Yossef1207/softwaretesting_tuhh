import string
from streamlink.plugins.ustvnow import USTVNow
from hypothesis import given, strategies as st
import base64

# ASCII-only strategy für IV und Key
ascii_key = st.text(min_size=16, max_size=32, alphabet=string.ascii_letters + string.digits)
ascii_iv = st.text(min_size=16, max_size=16, alphabet=string.ascii_letters + string.digits)

# Test 1: The return value is always Base64-encoded
@given(
    data=st.binary(min_size=1, max_size=1024),
    key=ascii_key,
    iv=ascii_iv
)
def test_output_is_base64(data, key, iv):
    result = USTVNow.encrypt_data(data, key, iv)
    decoded = base64.b64decode(result)
    assert isinstance(decoded, bytes)

# Test 2: Different data leads to different results
@given(
    data1=st.binary(min_size=16, max_size=128),
    data2=st.binary(min_size=16, max_size=128),
    key=ascii_key,
    iv=ascii_iv
)
def test_different_data_different_encryption(data1, data2, key, iv):
    # Data must be diferent to ensure different encryption results
    if data1 != data2:
        encrypted1 = USTVNow.encrypt_data(data1, key, iv)
        encrypted2 = USTVNow.encrypt_data(data2, key, iv)
        assert encrypted1 != encrypted2

# Test 3: Same inputs produce identical results
@given(
    data=st.binary(min_size=1, max_size=1024),
    key=ascii_key,
    iv=ascii_iv
)
def test_deterministic_output(data, key, iv):
    result1 = USTVNow.encrypt_data(data, key, iv)
    result2 = USTVNow.encrypt_data(data, key, iv)
    assert result1 == result2

# Test 4: The output is not empty
@given(
    data=st.binary(min_size=1, max_size=1024),
    key=ascii_key,
    iv=ascii_iv
)
def test_output_not_empty(data, key, iv):
    result = USTVNow.encrypt_data(data, key, iv)
    assert result != b""

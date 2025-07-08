import string
from streamlink.plugins.ustvnow import USTVNow
from hypothesis import given, settings, strategies as st

# Strategies for random data, key, and IV.
data_strategy = st.binary(min_size=0, max_size=64)
key_strategy = st.text(min_size=0, max_size=16, alphabet=string.ascii_letters + string.digits)
iv_strategy = st.text(min_size=16, max_size=16, alphabet=string.ascii_letters + string.digits)

@given(data=data_strategy, key=key_strategy, iv=iv_strategy) #@settings(max_examples=50)
def test_encrypt_decrypt_roundtrip(data, key, iv):
    encrypted = USTVNow.encrypt_data(data, key, iv)
    decrypted = USTVNow.decrypt_data(encrypted, key, iv)
    # After decrypting the ciphertext, we should get exactly the original data
    assert isinstance(decrypted, bytes)
    assert decrypted == data

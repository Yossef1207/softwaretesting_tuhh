import string
from hypothesis import strategies as st
from hypothesis.strategies import composite

# Strategies
ascii_key = st.text(min_size=16, max_size=32, alphabet=string.ascii_letters + string.digits)
ascii_iv = st.text(min_size=16, max_size=16, alphabet=string.ascii_letters + string.digits)
binary_data = st.binary(min_size=1, max_size=1024)
binary_data_16_128 = st.binary(min_size=16, max_size=128)

@composite
def example_test_output_is_base64(draw):
    return draw(binary_data), draw(ascii_key), draw(ascii_iv)

@composite
def example_test_different_data_different_encryption(draw):
    while True:
        data1 = draw(binary_data_16_128)
        data2 = draw(binary_data_16_128)
        if data1 != data2:
            break
    return data1, data2, draw(ascii_key), draw(ascii_iv)

@composite
def example_test_deterministic_output(draw):
    return draw(binary_data), draw(ascii_key), draw(ascii_iv)

@composite
def example_test_output_not_empty(draw):
    return draw(binary_data), draw(ascii_key), draw(ascii_iv)

# Get examples
def main():
    print("=== test_output_is_base64 ===")
    data, key, iv = example_test_output_is_base64().example()
    print("Data:", data)
    print("Key:", key)
    print("IV :", iv)
    print()

    print("=== test_different_data_different_encryption ===")
    data1, data2, key, iv = example_test_different_data_different_encryption().example()
    print("Data1:", data1)
    print("Data2:", data2)
    print("Key  :", key)
    print("IV   :", iv)
    print()

    print("=== test_deterministic_output ===")
    data, key, iv = example_test_deterministic_output().example()
    print("Data:", data)
    print("Key :", key)
    print("IV  :", iv)
    print()

    print("=== test_output_not_empty ===")
    data, key, iv = example_test_output_not_empty().example()
    print("Data:", data)
    print("Key :", key)
    print("IV  :", iv)

if __name__ == "__main__":
    main()

"""
Data: b'\xe6\xdff\xf7\xf2\xe1'
Key: Xzj7QVcqFqKaG0AS8uQ8lVXrdRrKJ62
IV : MqabCnlXQdLMEzfO

Data1: b"\xc7\xc9\x8eh\xd6\xb7\xee\t\x80\x7f\xb33\xbed\xd1\xeb\xdc\xe0\x1fV\xd7\x1d/\x95\x01\xb4Q\n\xdf\x85\x04T\xc8\x87\xb45\x86'\xb4\xb7"
Data2: b'\x8eg\x81\xd7\x18A9\xb8=&a\x1a@\xbd\x18\x8a\x9b\xac\xe8\xb3'
Key  : AY2VXI83VfzeE2VkNkJU
IV   : XNYda3Dj8qDJhUTg"""
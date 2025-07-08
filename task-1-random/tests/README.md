###  Install dependencies

You need `pytest`, `hypothesis` (if not already installed by Streamlink):

```bash
pip install pytest hypothesis 
```
RUN: ``pytest test_random_Maxim_Zilke.py`` to start the tests.

written by Maxim Zilke

--- 

## Test 1: Hypothesis-Based Tests for `encrypt_data` Function

This test suite verifies the behavior of the `encrypt_data` method from the `USTVNow` plugin in the Streamlink project using **property-based testing** with the [Hypothesis](https://hypothesis.readthedocs.io/) framework.

## What is being tested?

The method `USTVNow.encrypt_data(data, key, iv)` encrypts binary data using the AES algorithm in CBC mode with a padded plaintext. The tests ensure:

1. The output is valid Base64-encoded data.
2. Different inputs produce different encrypted outputs.
3. Identical inputs always produce identical results.
4. The output is never empty.

All tests use randomly generated input values within meaningful constraints to simulate realistic and edge-case usage scenarios.

## Input constraints

- `data`: Binary input between 1 and 1024 bytes.
- `key`: 16 to 32 ASCII alphanumeric characters (ensures predictable SHA256 encoding).
- `iv`: Exactly 16 ASCII alphanumeric characters (required length for AES-CBC IV).

These constraints prevent runtime errors due to encoding or incorrect IV length.

### 1. Install dependencies

You need `pytest`, `hypothesis`, and `pycryptodome` (if not already installed by Streamlink):

```bash
pip install pytest hypothesis pycryptodome
```

RUN: ``pytest test_encrypt_data_4.py`` to start the tests.

test_output_is_base64	-> Ensures the encrypted output is valid and decodable Base64.
test_different_data_different_encryption ->	Checks that different inputs lead to different encrypted results.
test_deterministic_output	-> Ensures the same inputs always lead to the same output.
test_output_not_empty -> Verifies that encryption always returns a non-empty result.

written by Yossef Al Buni

---


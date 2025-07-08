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
---
---
---
---
---







## Test 2: FileAdapter rejects invalid hostnames

RUN COMMAND# ``pytest -s test_FileAdapter.py -v``

**Purpose:** Ensure that the `FileAdapter.send` method (in **`streamlink.packages.requests_file.FileAdapter`**) rejects file URLs with disallowed hostnames by raising a `ValueError`. According to the Streamlink implementation, only empty hostnames or special cases like `"localhost"`, `"."`, `".."`, or `"-"` are permitted in `file://` URLs. Any other hostname should trigger an error.

**Why it’s useful:** This test checks the adapter’s input validation logic. By generating random hostnames that are *not* in the allowed list, we verify that the adapter consistently raises an error instead of attempting to open a forbidden file path. This prevents improper handling of invalid `file://` URLs and ensures security (no unintended file access).

**Example scenario:** If the code encounters a URL like `file://evil.com/path.txt`, it should refuse to handle it. The test uses Hypothesis to generate hostnames such as `"evil"` or `"example123"` and confirms that `FileAdapter.send` raises a `ValueError` each time. For instance, given the URL `file://notlocalhost/some.txt`, the adapter should raise a `ValueError` with the message about hostname not being permitted.

**What it verifies:** This test confirms that for any generated hostname outside the allowed list, `FileAdapter.send` will raise a `ValueError`. In other words, the property is that **disallowed hostnames are never accepted**.

**Why it’s useful:** It verifies the security check in the file adapter. Ensuring `ValueError` is raised for invalid hosts means the adapter won’t accidentally open files from unintended locations (e.g., treating `file://evil.com/etc/passwd` as a local file). The property-based approach covers a wide range of random host strings, increasing confidence that the validation isn’t brittle or missed for some edge-case hostname.

**Typical output:** The test doesn’t produce a direct output on success (it will pass silently if all generated cases raise the error as expected). If there’s a failure (i.e., some invalid hostname did **not** raise an error), the test would fail with an assertion similar to: *"`FailedExample: host='abc' did not raise ValueError`"*. In normal operation, each generated `host` like `"abc"`, `"xyz123"`, or `"my-host"` triggers the `ValueError`, and the test passes.


## Test 3: parse_params

RUN COMMAND# ``pytest -s test_parse_params.py -v``

**Function description:**  
The `parse_params` function takes a string (or `None`) and returns a dictionary of parsed parameters. It uses a regular expression to extract key-value pairs from the input string. For each match, it attempts to safely evaluate the value using Python’s `ast.literal_eval` (which parses Python literals like numbers, strings, lists, etc.). If evaluation fails, the raw string is used as the value. If the input is `None` or empty, an empty dictionary is returned.

**Why it’s useful:**  
This function is designed to flexibly parse parameter strings, such as those found in plugin options or configuration files. By using `ast.literal_eval`, it can handle a variety of value types (e.g., integers, booleans, lists) while avoiding the security risks of `eval`. The function is robust against malformed input: if a value cannot be parsed, it simply stores the original string.

**What the test does:**  
The property-based test uses Hypothesis to generate a wide range of random strings (including `None`). For each generated input, it calls `parse_params` and asserts that the result is always a dictionary. This ensures the function never crashes or returns an unexpected type, no matter what input it receives.

**Why this is important:**  
- **Robustness:** The test guarantees that `parse_params` gracefully handles all possible input, including edge cases like empty strings, random text, or `None`.
- **Type safety:** It ensures the function always returns a dictionary, which is important for downstream code that relies on this contract.
- **Security:** By using `ast.literal_eval` within a try/except block, the function avoids executing arbitrary code and is safe against malicious input.

**Example scenario:**  
- Input: `None` → Output: `{}`
- Input: `"foo=1,bar='baz'"` → Output: `{'foo': 1, 'bar': 'baz'}`
- Input: `"x=[1,2,3],y=True"` → Output: `{'x': [1, 2, 3], 'y': True}`
- Input: `"invalid=not_a_literal"` → Output: `{'invalid': 'not_a_literal'}` (since `not_a_literal` cannot be evaluated as a Python literal)

**Typical output:**  
The test will pass silently if all generated inputs result in a dictionary. If the function ever returns a non-dictionary or raises an exception, the test will fail, indicating a problem with input handling.


## Test 4: USTVNow encryption/decryption round-trip

RUN COMMAND# ``pytest -s test_encrypt_roundtrip.py -v``

**Purpose:** Verify that the custom encryption and decryption in the **USTVNow plugin** (`streamlink.plugins.ustvnow.USTVNow.encrypt_data` and `decrypt_data`) are consistent. We generate random binary data (plaintext), a random key, and a random IV (initialization vector), then assert that decrypting the encrypted data returns the original plaintext. This tests the symmetry of the encryption scheme.

**Why it’s useful:** The USTVNow plugin uses a bespoke AES encryption (with key/IV transformations) to communicate with the service’s API. It’s crucial that encryption and decryption are inverses; otherwise, data would be corrupted or the plugin would fail to authenticate. By testing random bytes and random keys/IVs, we ensure that for all cases the `decrypt_data` correctly reverses `encrypt_data`.

**Example scenario:** If `data = b"hello world"`, with some `key = "ABC123"` and `iv = "XYZ7890123456789"` (16 characters), then `decrypt_data(encrypt_data(data, key, iv), key, iv)` should yield `b"hello world"` again. The test will try numerous random byte sequences and keys/IVs (including edge cases like empty data or very short keys) to validate this property.

**What it verifies:** For every combination of input bytes, key, and 16-byte IV generated:

* The encryption function returns some output (presumably base64-encoded bytes).
* Decryption of that output (with the same key and IV) yields the original input `data` exactly. This confirms that no randomness or external state causes mismatch – the encryption is deterministic and correctly reversible with the same parameters.

**Why it’s useful:** It catches any errors in padding, key derivation, or encoding. For instance, if the plugin’s `encrypt_data` or `decrypt_data` had an off-by-one error in padding or mis-used the key/IV, this round-trip test would fail for some random input. By testing a variety of lengths and content (including empty bytes, which test padding edge cases), we gain confidence that the cryptographic routine works for all typical inputs the plugin might encounter.

**Typical output:** The test will generally pass without any output if the encryption/decryption are implemented correctly. Internally, it might generate cases like:

* `data = b''` (empty bytes), random key/IV -> encrypted (some bytes) -> decrypted equals `b''`.
* `data = b'\x00\x01\x02'`, key `'abc'`, iv `'1234567890abcdef'` -> decrypted matches original bytes.
  If something were wrong (say decryption returned a different value), an assertion error would occur, e.g.: *`AssertionError: assert b'\x00\x01' == b'\x00\x01\x00'`*, which would indicate the decrypted data isn’t identical (perhaps padding wasn’t removed correctly). In successful runs, each example yields `decrypted == data`, and the property holds.

## Test 5: iterate_streams

RUN COMMAND# `pytest -s test_iterate_streams.py -v`

**Function description:**  
The `iterate_streams` function takes a list of `(name, stream)` pairs. Each `stream` can either be a single stream object (such as a string or another type) or a list of stream objects. The function iterates over the input list and, for each entry:
- If the `stream` is a list, it yields a tuple `(name, sub_stream)` for each item in the list.
- If the `stream` is not a list, it yields the tuple `(name, stream)` directly.

This effectively "flattens" any nested lists of streams, so that the output is always a sequence of `(name, stream)` pairs, regardless of whether the original input had single streams or lists of streams.

**Why it’s useful:**  
This function is helpful when you want to process a collection of streams where some entries might be grouped (as lists) and others are single items. By flattening the structure, downstream code can handle all streams uniformly, without worrying about whether each entry is a list or not.

**What the test does:**  
The property-based test uses Hypothesis to generate a wide variety of random input lists. Each list contains tuples of:
- a random string as the stream name,
- either a random string (representing a single stream) or a list of random strings (representing multiple streams).

For each generated input, the test calls `iterate_streams` and collects the output. It then checks that every yielded item is a tuple where the first element (`name`) is always a string. This ensures that the function correctly flattens the input and maintains the expected output structure.

**Why this is important:**  
- **Robustness:** The test ensures that `iterate_streams` can handle any combination of single streams and lists of streams, including edge cases like empty lists or deeply nested lists.
- **Type safety:** It guarantees that the output always consists of `(name, stream)` tuples with the correct types, which is important for any code that consumes this output.
- **Uniformity:** By flattening the structure, the function simplifies further processing and reduces the risk of bugs caused by unexpected input formats.

**Example scenario:**  
- Input: `[("live", "stream1"), ("vod", ["stream2", "stream3"])]`
- Output: `[("live", "stream1"), ("vod", "stream2"), ("vod", "stream3")]`

- Input: `[("main", ["a", "b"]), ("alt", "c")]`
- Output: `[("main", "a"), ("main", "b"), ("alt", "c")]`

**Typical output:**  
The test will pass silently if all generated inputs result in the correct output structure. If the function ever yields a tuple where the name is not a string, or if it fails to flatten the streams correctly, the test will fail.


written by Yossef Al Buni







###  Install dependencies

You need `pytest`, `hypothesis` (if not already installed by Streamlink):

```bash
pip install pytest hypothesis 
```

RUN: ``pytest test_random_Maxim_Zilke.py`` to start the tests.

written by Maxim Zilke
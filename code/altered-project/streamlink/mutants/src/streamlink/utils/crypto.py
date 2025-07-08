# ruff: noqa: F401
import hashlib


# re-export pycryptodome / pycryptodomex stuff in a single place
# so packagers don't have to maintain dozens of patches
try:
    # pycryptodome (drop-in replacement for the old PyCrypto library)
    from Crypto.Cipher import AES, PKCS1_v1_5
    from Crypto.Hash import SHA256
    from Crypto.PublicKey import RSA
    from Crypto.Util.Padding import pad, unpad
except ImportError:  # pragma: no cover
    # pycryptodomex (independent of the old PyCrypto library)
    from Cryptodome.Cipher import AES, PKCS1_v1_5  # type: ignore
    from Cryptodome.Hash import SHA256  # type: ignore
    from Cryptodome.PublicKey import RSA  # type: ignore
    from Cryptodome.Util.Padding import pad, unpad  # type: ignore
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


def x_evp_bytestokey__mutmut_orig(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_1(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = None
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_2(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b"XXXX"
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_3(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_4(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_5(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_6(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) <= key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_7(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len - iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_8(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = None
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_9(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(None).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_10(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i - password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_11(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password - salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_12(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d = d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_13(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d -= d_i
    return d[:key_len], d[key_len : key_len + iv_len]


def x_evp_bytestokey__mutmut_14(password, salt, key_len, iv_len):
    """
    Python implementation of OpenSSL's EVP_BytesToKey()
    :param password: or passphrase
    :param salt: 8 byte salt
    :param key_len: length of key in bytes
    :param iv_len:  length of IV in bytes
    :return: (key, iv)
    """
    d = d_i = b""
    while len(d) < key_len + iv_len:
        d_i = hashlib.md5(d_i + password + salt).digest()
        d += d_i
    return d[:key_len], d[key_len : key_len - iv_len]

x_evp_bytestokey__mutmut_mutants : ClassVar[MutantDict] = {
'x_evp_bytestokey__mutmut_1': x_evp_bytestokey__mutmut_1, 
    'x_evp_bytestokey__mutmut_2': x_evp_bytestokey__mutmut_2, 
    'x_evp_bytestokey__mutmut_3': x_evp_bytestokey__mutmut_3, 
    'x_evp_bytestokey__mutmut_4': x_evp_bytestokey__mutmut_4, 
    'x_evp_bytestokey__mutmut_5': x_evp_bytestokey__mutmut_5, 
    'x_evp_bytestokey__mutmut_6': x_evp_bytestokey__mutmut_6, 
    'x_evp_bytestokey__mutmut_7': x_evp_bytestokey__mutmut_7, 
    'x_evp_bytestokey__mutmut_8': x_evp_bytestokey__mutmut_8, 
    'x_evp_bytestokey__mutmut_9': x_evp_bytestokey__mutmut_9, 
    'x_evp_bytestokey__mutmut_10': x_evp_bytestokey__mutmut_10, 
    'x_evp_bytestokey__mutmut_11': x_evp_bytestokey__mutmut_11, 
    'x_evp_bytestokey__mutmut_12': x_evp_bytestokey__mutmut_12, 
    'x_evp_bytestokey__mutmut_13': x_evp_bytestokey__mutmut_13, 
    'x_evp_bytestokey__mutmut_14': x_evp_bytestokey__mutmut_14
}

def evp_bytestokey(*args, **kwargs):
    result = _mutmut_trampoline(x_evp_bytestokey__mutmut_orig, x_evp_bytestokey__mutmut_mutants, args, kwargs)
    return result 

evp_bytestokey.__signature__ = _mutmut_signature(x_evp_bytestokey__mutmut_orig)
x_evp_bytestokey__mutmut_orig.__name__ = 'x_evp_bytestokey'


def x_decrypt_openssl__mutmut_orig(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_1(data, passphrase, key_length=33):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_2(data, passphrase, key_length=32):
    if data.startswith(None):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_3(data, passphrase, key_length=32):
    if data.startswith(b"XXSalted__XX"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_4(data, passphrase, key_length=32):
    if data.startswith(b"salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_5(data, passphrase, key_length=32):
    if data.startswith(b"SALTED__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_6(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_7(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = None
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_8(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = None
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_9(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(None, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_10(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, None, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_11(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, None, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_12(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, None)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_13(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_14(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_15(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_16(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, )
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_17(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = None
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_18(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(None, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_19(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, None, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_20(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, None)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_21(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_22(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_23(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, )
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_24(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = None
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_25(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(None)
        return unpad_pkcs5(out)


def x_decrypt_openssl__mutmut_26(data, passphrase, key_length=32):
    if data.startswith(b"Salted__"):
        salt = data[len(b"Salted__") : AES.block_size]
        key, iv = evp_bytestokey(passphrase, salt, key_length, AES.block_size)
        d = AES.new(key, AES.MODE_CBC, iv)
        out = d.decrypt(data[AES.block_size :])
        return unpad_pkcs5(None)

x_decrypt_openssl__mutmut_mutants : ClassVar[MutantDict] = {
'x_decrypt_openssl__mutmut_1': x_decrypt_openssl__mutmut_1, 
    'x_decrypt_openssl__mutmut_2': x_decrypt_openssl__mutmut_2, 
    'x_decrypt_openssl__mutmut_3': x_decrypt_openssl__mutmut_3, 
    'x_decrypt_openssl__mutmut_4': x_decrypt_openssl__mutmut_4, 
    'x_decrypt_openssl__mutmut_5': x_decrypt_openssl__mutmut_5, 
    'x_decrypt_openssl__mutmut_6': x_decrypt_openssl__mutmut_6, 
    'x_decrypt_openssl__mutmut_7': x_decrypt_openssl__mutmut_7, 
    'x_decrypt_openssl__mutmut_8': x_decrypt_openssl__mutmut_8, 
    'x_decrypt_openssl__mutmut_9': x_decrypt_openssl__mutmut_9, 
    'x_decrypt_openssl__mutmut_10': x_decrypt_openssl__mutmut_10, 
    'x_decrypt_openssl__mutmut_11': x_decrypt_openssl__mutmut_11, 
    'x_decrypt_openssl__mutmut_12': x_decrypt_openssl__mutmut_12, 
    'x_decrypt_openssl__mutmut_13': x_decrypt_openssl__mutmut_13, 
    'x_decrypt_openssl__mutmut_14': x_decrypt_openssl__mutmut_14, 
    'x_decrypt_openssl__mutmut_15': x_decrypt_openssl__mutmut_15, 
    'x_decrypt_openssl__mutmut_16': x_decrypt_openssl__mutmut_16, 
    'x_decrypt_openssl__mutmut_17': x_decrypt_openssl__mutmut_17, 
    'x_decrypt_openssl__mutmut_18': x_decrypt_openssl__mutmut_18, 
    'x_decrypt_openssl__mutmut_19': x_decrypt_openssl__mutmut_19, 
    'x_decrypt_openssl__mutmut_20': x_decrypt_openssl__mutmut_20, 
    'x_decrypt_openssl__mutmut_21': x_decrypt_openssl__mutmut_21, 
    'x_decrypt_openssl__mutmut_22': x_decrypt_openssl__mutmut_22, 
    'x_decrypt_openssl__mutmut_23': x_decrypt_openssl__mutmut_23, 
    'x_decrypt_openssl__mutmut_24': x_decrypt_openssl__mutmut_24, 
    'x_decrypt_openssl__mutmut_25': x_decrypt_openssl__mutmut_25, 
    'x_decrypt_openssl__mutmut_26': x_decrypt_openssl__mutmut_26
}

def decrypt_openssl(*args, **kwargs):
    result = _mutmut_trampoline(x_decrypt_openssl__mutmut_orig, x_decrypt_openssl__mutmut_mutants, args, kwargs)
    return result 

decrypt_openssl.__signature__ = _mutmut_signature(x_decrypt_openssl__mutmut_orig)
x_decrypt_openssl__mutmut_orig.__name__ = 'x_decrypt_openssl'


def x_unpad_pkcs5__mutmut_orig(padded):
    return padded[: -padded[-1]]


def x_unpad_pkcs5__mutmut_1(padded):
    return padded[: +padded[-1]]


def x_unpad_pkcs5__mutmut_2(padded):
    return padded[: -padded[+1]]


def x_unpad_pkcs5__mutmut_3(padded):
    return padded[: -padded[-2]]

x_unpad_pkcs5__mutmut_mutants : ClassVar[MutantDict] = {
'x_unpad_pkcs5__mutmut_1': x_unpad_pkcs5__mutmut_1, 
    'x_unpad_pkcs5__mutmut_2': x_unpad_pkcs5__mutmut_2, 
    'x_unpad_pkcs5__mutmut_3': x_unpad_pkcs5__mutmut_3
}

def unpad_pkcs5(*args, **kwargs):
    result = _mutmut_trampoline(x_unpad_pkcs5__mutmut_orig, x_unpad_pkcs5__mutmut_mutants, args, kwargs)
    return result 

unpad_pkcs5.__signature__ = _mutmut_signature(x_unpad_pkcs5__mutmut_orig)
x_unpad_pkcs5__mutmut_orig.__name__ = 'x_unpad_pkcs5'

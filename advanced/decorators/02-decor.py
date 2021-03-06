# 02-decor.py
from hashlib import sha256, sha512, shake_256, blake2b, blake2s, md5
import os
import time


# Sizes in bytes
ONE_KB = 1024
ONE_MB = 1024 * ONE_KB
TEN_MB = 10 * ONE_MB
HUNDRED_MB = 10 * TEN_MB


def timeit(fn):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = fn(*args, **kwargs)
        print(f'{fn.__name__}: {time.time() - t0:.02f}s')
        return res
    return wrapper


def mktestdata(size=HUNDRED_MB):
    """Return random binary data of the given size."""

    data = b''
    chunk = ONE_MB
    while size:
        if size <= chunk:
            chunk = size

        data += os.urandom(chunk)
        size -= chunk
    return data


def test_sha256(data):
    return sha256(data).hexdigest()


def test_sha512(data):
    return sha512(data).hexdigest()


def test_shake_256(data):
    return shake_256(data).hexdigest()


def test_blake2b(data):
    return blake2b(data).hexdigest()


def test_blake2s(data):
    return blake2s(data).hexdigest()


def test_md5(data):
    return md5(data).hexdigest()


test_sha256 = timeit(test_sha256)
test_sha512 = timeit(test_sha512)
test_shake_256 = timeit(test_shake_256)
test_blake2b = timeit(test_blake2b)
test_blake2s = timeit(test_blake2s)
test_md5 = timeit(test_md5)

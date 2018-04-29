# decor2.py
from hashlib import sha256, sha512, shake_256, blake2b, blake2s, md5
import os
import time


# Sizes in bytes
ONE_KB = 1024
ONE_MB = 1024 * ONE_KB
TEN_MB = 10 * ONE_MB
HUNDRED_MB = 10 * TEN_MB


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
    t0 = time.time()
    res = sha256(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res


def test_sha512(data):
    t0 = time.time()
    res = sha512(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res


def test_shake_256(data):
    t0 = time.time()
    res = shake_256(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res


def test_blake2b(data):
    t0 = time.time()
    res = blake2b(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res


def test_blake2s(data):
    t0 = time.time()
    res = blake2s(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res


def test_md5(data):
    t0 = time.time()
    res = md5(data).hexdigest()
    print(f'test_sha256: {time.time() - t0:.02f}')
    return res

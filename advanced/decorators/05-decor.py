# 05-decor.py
from functools import wraps, partial
import hashlib
import os
import time


# Sizes in bytes
ONE_KB = 1024
ONE_MB = 1024 * ONE_KB
TEN_MB = 10 * ONE_MB
HUNDRED_MB = 10 * TEN_MB


def timeit(fn):
    @wraps(fn)
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


@timeit
def test_hash(data, hash_fn):
    return getattr(hashlib, hash_fn)(data).hexdigest()


test_sha256 = partial(test_hash, hash_fn='sha256')
test_sha512 = partial(test_hash, hash_fn='sha512')
test_shake_256 = partial(test_hash, hash_fn='shake_256')
test_blake2b = partial(test_hash, hash_fn='blake2b')
test_blake2s = partial(test_hash, hash_fn='blake2s')
test_md5 = partial(test_hash, hash_fn='md5')

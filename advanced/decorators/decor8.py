# decor8.py
from functools import wraps, partial
import hashlib
import os
import time


# Sizes in bytes
ONE_KB = 1024
ONE_MB = 1024 * ONE_KB                      # <-- more realistic size
TEN_MB = 10 * ONE_MB
HUNDRED_MB = 10 * TEN_MB


def timeit_ntimes(n=10):
    def timeit(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            t0 = time.time()
            for _ in range(n):
                res = fn(*args, **kwargs)
            print(f'{fn.__name__}: {(time.time() - t0) / n:.04f}s')
            return res
        return wrapper
    return timeit


def mktestdata(size=ONE_MB):
    """Return random binary data of the given size."""

    data = b''
    chunk = ONE_MB
    while size:
        if size <= chunk:
            chunk = size

        data += os.urandom(chunk)
        size -= chunk
    return data


@timeit_ntimes(100)
def test_hash(data, hash_fn):
    return getattr(hashlib, hash_fn)(data).hexdigest()


# The above is equivalent to
# decorator = timeit_ntimes(100)
# test_hash = decorator(test_hash)
#
# This means that I can pre-configure a decorator and use it several times:
timeit = timeit_ntimes(1)


@timeit
def foo():
    time.sleep(1)


test_sha256 = partial(test_hash, hash_fn='sha256')
test_sha512 = partial(test_hash, hash_fn='sha512')
test_shake_256 = partial(test_hash, hash_fn='shake_256')
test_blake2b = partial(test_hash, hash_fn='blake2b')
test_blake2s = partial(test_hash, hash_fn='blake2s')
test_md5 = partial(test_hash, hash_fn='md5')

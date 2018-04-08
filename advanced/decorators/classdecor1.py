from functools import wraps
import time


def timeit(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = fn(*args, **kwargs)
        print(f'{fn.__name__}: {time.time() - t0:.04f}s')
        return res
    return wrapper


class Foo:
    @timeit
    def fast_method(self):
        time.sleep(.1)
        return

    @timeit
    def slow_method(self):
        time.sleep(1)
        return

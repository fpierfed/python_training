# classdecor2.py
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


def time_methods(cls):
    for name, attribute in vars(cls).items():
        if callable(attribute):
            setattr(cls, name, timeit(attribute))
    return cls


@time_methods
class Foo:
    def fast_method(self):
        time.sleep(.1)
        return

    def slow_method(self):
        time.sleep(1)
        return

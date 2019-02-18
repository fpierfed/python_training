# 01-context_namager.py
"""
There are two main ways to create contect managers: using classes or
using coroutines. For coroutines, we need to use the contextlib module.
"""
from contextlib import contextmanager
import sys


@contextmanager
def my_manager(*args, **kwargs):
    instr = ', '.join([str(a) for a in args] +
                      [f'{k}={v}' for k, v in kwargs.items()])
    print(f'Entering with input {instr}')

    # Run whatever the use wants
    try:
        yield 'something'
    except:                                                             # noqa
        exc_type, exc_value, exc_traceback = sys.exc_info()
        print(exc_type, exc_value, exc_traceback)
        print('Cleaning up')
    else:
        print('All good')
    finally:
        print('Exiting')


# Same thing with a class
class MyManager:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __enter__(self):
        instr = ', '.join([str(a) for a in self.args] +
                          [f'{k}={v}' for k, v in self.kwargs.items()])
        print(f'Entering with input {instr}')
        return 'something'

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type is not None:
            print(exc_type, exc_value, exc_traceback)
            print('Cleaning up')
        else:
            print('All good')
        print('Exiting')
        return True                     # Suppress the exception propagation


if __name__ == '__main__':
    with my_manager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        for i in range(5):
            print(i)

    with MyManager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        for i in range(5):
            print(i)

    # What about exceptions?
    with my_manager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        print(1 / 0)

    with MyManager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        print(1 / 0)

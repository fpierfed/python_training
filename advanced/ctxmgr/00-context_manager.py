# 00-context_namager.py
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


if __name__ == '__main__':
    with my_manager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        for i in range(5):
            print(i)

    # What about exceptions?
    with my_manager(1, 2, 3, d=4, e=5) as foo:
        print(f'foo = {foo}')
        print(1 / 0)

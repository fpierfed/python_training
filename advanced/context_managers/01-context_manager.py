# 01-context_namager.py
"""
There are two main ways to create contect managers: using classes or
using coroutines. For coroutines, we need to use the contextlib module.
"""
from contextlib import contextmanager


@contextmanager
def my_file(fname, mode='r'):
    print('   Setup')
    f = open(fname, mode)

    try:
        yield f
    except Exception:
        raise
    else:
        print('   All good')
    finally:
        f.close()
        print('   Cleanup')


if __name__ == '__main__':
    fname = '/tmp/foo'
    msg = 'Hello'

    with my_file(fname, 'w') as f:
        f.write(msg)
        print(f'Wrote {msg}')

    with my_file(fname) as f:
        inmsg = f.readline()
        assert inmsg == msg, f'{inmsg} != {msg}'
        print(f'Got {msg}')

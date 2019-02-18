# 00-context_manager.py
"""
There are two main ways to create contect managers: using classes or
using coroutines. For coroutines, we need to use the contextlib module.
"""


class MyFile:
    def __init__(self, fname, mode='r'):
        self._fname = fname
        self._mode = mode
        self._f = None

    def __enter__(self):
        print('  Setup')
        self._f = open(self._fname, self._mode)
        return self._f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('  Cleanup')
        self._f.close()

        if exc_type is not None:
            print(exc_type, exc_value, exc_traceback)
            return False
        return True


if __name__ == '__main__':
    fname = '/tmp/foo'
    msg = 'Hello'

    with MyFile(fname, 'w') as f:
        f.write(msg)
        print(f'Wrote {msg}')

    with MyFile(fname) as f:
        inmsg = f.readline()
        assert inmsg == msg, f'{inmsg} != {msg}'
        print(f'Got {msg}')

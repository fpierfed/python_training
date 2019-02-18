# 00-context_manager.py


class MyFile:
    def __init__(self, fname, mode='r'):
        self._fname = fname
        self._mode = mode
        self._f = None

    def __enter__(self):
        print('__enter__()')
        self._f = open(self._fname, self._mode)
        return self._f

    def __exit__(self, exc_type, exc_value, exc_traceback):
        print('__exit__()')
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
        assert f.readline() == msg
        print(f'Got {msg}')

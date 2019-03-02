# coro1.py
def foo():
    print('Hello')
    yield
    print('World')
    yield
    print('Bye')
    yield
    print('World')


if __name__ == '__main__':
    g = foo()
    next(g)
    next(g)
    next(g)
    next(g)

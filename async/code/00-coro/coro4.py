# coro4.py
def foo():
    yield 1
    yield 2
    return 3


def bar(coro):
    yield from coro
    yield 99


if __name__ == '__main__':
    g = bar(foo())
    next(g)
    next(g)
    next(g)
    next(g)

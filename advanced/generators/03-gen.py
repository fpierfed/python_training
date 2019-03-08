# 03-gen.py


def subgen(n):
    while n >= 0:
        yield n
        n -= 1
    # raise Exception('foo')
    return 99


def gen():
    try:
        yield from subgen(3)
    except Exception as e:
        print('Got', e)
    yield 42


# gen is equivalent to this:
def raw_gen():
    g = subgen(3)
    try:
        while True:
            try:
                yield next(g)
            except StopIteration:
                break
    except Exception as e:
        print('Got', e)
    yield 42

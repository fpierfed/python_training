# gen3.py


def subgen():
    yield 42


def gen():
    yield from subgen()


# gen is equivalent to
def raw_gen():
    g = subgen()
    while True:
        try:
            yield next(g)
        except StopIteration as e:
            return e.value

# gen1.py
# Generators can spit out values, return (only in Python3) and receive values


def echo(n):
    value = None
    while n:
        value = yield value
        n -= 1
    return value


if __name__ == '__main__':
    g = echo(5)

    # Init the genetaor
    g.send(None)            # equivalent to next(g), equivalent to g.__next__()

    print(g.send('Hello'))
    print(g.send('Francesco'))
    print(g.send('Bye'))
    print(g.send('Francesco'))
    try:
        print(g.send('Ops!'))
    except StopIteration as e:
        print(f'Returned {e.value}')

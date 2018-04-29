# iter3.py
def simple_range(n):
    _current = 0
    while _current < n:
        yield _current
        _current += 1


if __name__ == '__main__':
    for i in simple_range(10):
        print(i)

    # This is equivalent to
    g = simple_range(10)
    i = g.__iter__()                                    # i is g by the way!
    while True:
        try:
            print(i.__next__())
        except StopIteration:
            break

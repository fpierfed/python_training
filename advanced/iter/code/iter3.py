def simple_range(n):
    _current = 0
    while _current < n:
        yield _current
        _current += 1


if __name__ == '__main__':
    for i in simple_range(10):
        print(i)

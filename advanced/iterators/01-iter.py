# 01-iter.py
class SimpleRange:
    def __init__(self, n):
        self.n = n
        self._current = None

    def __iter__(self):
        self._current = -1
        return self

    def __next__(self):
        self._current += 1
        if self._current < self.n:
            return self._current
        raise StopIteration()


if __name__ == '__main__':
    simple_range = SimpleRange(10)
    for x in simple_range:
        print(x)

# 06-list.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        """Return user-friendly string representation."""
        return f'({self.x}, {self.y})'

    def __repr__(self):
        """Return developer-friendly string representation."""
        return f'{self.__class__.__name__}({self.x!r}, {self.y!r})'


class Path:
    def __init__(self, points):
        self._points = points                                   # <-- "private"

    def __str__(self):
        return f'Path of {len(self._points)} Points'

    def __repr__(self):
        return f'{self.__class__.__name__}({self._points!r})'

    def __len__(self):
        return len(self._points)

    def __getitem__(self, key):
        return self._points.__getitem__(key)

    def __setitem__(self, key, val):
        if not isinstance(val, Point):
            raise TypeError('expecting a Point')
        return self._points.__setitem__(key, val)

    def __delitem__(self, key):
        return self._points.__delitem__(key)

    def __contains__(self, obj):
        return self._points.__contains__(obj)

    def append(self, item):
        if not isinstance(item, Point):
            raise TypeError('expecting a Point')
        return self._points.append(item)

    def __getattr__(self, key):
        return getattr(self._points, key)


if __name__ == '__main__':
    path = Path([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])

    print('Path:')
    for i in range(len(path)):
        print(f'  {path[i]!r}')
    print(f'Total: {len(path)} point(s)')

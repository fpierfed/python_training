# 05-list.py
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

    def length(self):
        return len(self._points)

    def point_at(self, index):
        return self._points[index]


if __name__ == '__main__':
    path = Path([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])

    print('Path:')
    n = path.length()
    for i in range(n):
        print(f'  {path.point_at(i)!r}')
    print(f'Total: {n} point(s)')

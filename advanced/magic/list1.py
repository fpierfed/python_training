# list1.py
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
        self.points = points

    def __str__(self):
        return f'Path of {len(self.points)} Points'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.points!r})'


if __name__ == '__main__':
    path = Path([Point(0, 0), Point(0, 1), Point(1, 1), Point(1, 0)])

    print('Path:')
    for p in path.points:
        print(f'  {p!r}')
    print(f'Total: {len(path.points)} point(s)')

# point2.py
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


if __name__ == '__main__':
    p = Point(1, 2)
    print(f'Users: this is my new point: {p}')
    print(f'Developers: p = {p!r}')

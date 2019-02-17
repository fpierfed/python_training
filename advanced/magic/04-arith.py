# arith2.py
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

    def __add__(self, other):
        if isinstance(other, Point):
            x = self.x + other.x
            y = self.y + other.y
        if isinstance(other, tuple) and len(other) == 2:
            x = self.x + other[0]
            y = self.y + other[1]
        else:
            raise TypeError('expecting a 2-element tuple')
        return self.__class__(x, y)


if __name__ == '__main__':
    p = Point(0, 0)
    print(f'p = {p!r}')

    # Add a shift to p (i.e. move p)
    p += (10, 20)
    print(f'p + (10, 20) = {p!r}')

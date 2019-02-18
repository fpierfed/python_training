# 00-datacl.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point at ({self.x}, {self.y})'

    def __repr__(self):
        return f'Point({self.x!r}, {self.y!r})'


p = Point(1, 2)
print(f'str(p) = {p}')
print(f'repr(p) = {p!r}')

# 00-print.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == '__main__':
    p = Point(1, 2)
    print(f'Users: this is my new point: {p}')
    print(f'Developers: p = {p!r}')

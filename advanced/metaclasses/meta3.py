# meta3.py
class MyType(type):
    def __new__(meta, name, bases, dct):
        print(f'MyType.__new__({meta!r}, {name}, {bases}, {dct})')
        return super().__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f'MyType.__init__({cls!r}, {name}, {bases}, {dct})')
        super().__init__(name, bases, dct)


class Point(metaclass=MyType):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'

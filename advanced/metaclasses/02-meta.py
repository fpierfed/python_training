# 02-meta.py
class MyType(type):
    def __new__(meta, name, bases, dct):
        print(f'MyType.__new__({meta!r}, {name}, {bases}, {dct})')
        return super().__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):
        print(f'MyType.__init__({cls!r}, {name}, {bases}, {dct})')
        super().__init__(name, bases, dct)


def __init__(self, x, y):
    self.x = x
    self.y = y


def __repr__(self):
    return f'Point({self.x}, {self.y})'


def __str__(self):
    return f'{self.x}, {self.y}'


name = 'Point'
dct = {
    '__init__': __init__,
    '__repr__': __repr__,
    '__str__': __str__}
bases = ()          # equivalent in the call below to (object, )

Point = MyType(name, bases, dct)

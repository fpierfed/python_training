class MyType(type):
    def __new__(meta, name, bases, methods):
        print(f'About to create a new {name} class')
        return super().__new__(meta, name, bases, methods)


def __init__(self, x, y):
    self.x = x
    self.y = y


def __repr__(self):
    return f'Point({self.x}, {self.y})'


def __str__(self):
    return f'{self.x}, {self.y}'


name = 'Point'
methods = {
    '__init__': __init__,
    '__repr__': __repr__,
    '__str__': __str__}
bases = ()          # equivalent in the call below to (object, )

Point = MyType(name, bases, methods)

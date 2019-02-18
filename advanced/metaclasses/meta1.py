# meta1.py
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f'Point({self.x}, {self.y})'
#
#     def __str__(self):
#         return f'{self.x}, {self.y}'
#
#
# The code above is equivalent to this below:


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

Point = type(name, bases, dct)

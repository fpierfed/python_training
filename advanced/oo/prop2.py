# prop2.py
from math import pi
from numbers import Number


def check_type(name, required_type):
    ivar_name = f'_{name}'

    @property
    def ivar(self):
        return getattr(self, ivar_name)

    @ivar.setter
    def ivar(self, value):
        if not isinstance(value, required_type):
            raise TypeError(f'expecting a {required_type.__name__}')
        setattr(self, ivar_name, value)
    return ivar


class Point:
    x = check_type('x', Number)
    y = check_type('y', Number)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'


class Circle:
    radius = check_type('radius', Number)
    center = check_type('center', Point)

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return f'Circle({self.center!r}, {self.radius!r})'

    def __str__(self):
        return f'Circle of radius {self.radius} at {self.center}'

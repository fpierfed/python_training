# prop.py
from math import pi
from numbers import Number


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        if not isinstance(value, Number):
            raise TypeError('expecting a number')
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if not isinstance(value, Number):
            raise TypeError('expecting a number')
        self._y = value

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        if not isinstance(value, Point):
            raise TypeError('expecting a Point')
        self._center = value

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if not isinstance(value, Number):
            raise TypeError('expecting a number')
        self._radius = value

    @property
    def area(self):
        return pi * self.radius ** 2

    def __repr__(self):
        return f'Circle({self.center!r}, {self.radius!r})'

    def __str__(self):
        return f'Circle of radius {self.radius} at {self.center}'

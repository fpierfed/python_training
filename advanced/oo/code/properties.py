from collections import namedtuple
from math import pi, sqrt


Point = namedtuple('Point', ('x', 'y'))


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError('radius cannot be negative')
        self._radius = value

    @property
    def area(self):
        return pi * self.radius ** 2

    @area.setter
    def area(self, value):
        if value < 0:
            # What???
            raise ValueError('area cannot be negative')
        self.radius = sqrt(value / pi)

    # @area.deleter
    # def area(self):
    #     print('Good by cruel word')
    #     print('Just kidding!')

    @property
    def center(self):
        return self._center

    @center.setter
    def center(self, value):
        if not isinstance(value, Point):
            raise TypeError('must be an instance of Point')
        self._center = value

from collections import namedtuple
from math import pi, sqrt


Point = namedtuple('Point', ('x', 'y'))


def type_check(name, required_type):
    ivar_name = f'_{name}'

    @property
    def ivar(instance):
        return getattr(instance, ivar_name)

    @ivar.setter
    def ivar(instance, value):
        if not isinstance(value, required_type):
            raise TypeError(f'expected {required_type.__name__}')
        setattr(instance, ivar_name, value)

    # return the ivar property so that it can be used by a class.
    return ivar


FloatType = lambda name: type_check(name, float)                        # noqa
PointType = lambda name: type_check(name, Point)                        # noqa


class Circle:
    radius = FloatType('radius')
    center = PointType('center')

    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    @area.setter
    def area(self, value):
        if value < 0:
            # What???
            raise ValueError('area cannot be negative')
        self.radius = sqrt(value / pi)

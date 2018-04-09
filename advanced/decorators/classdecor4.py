from math import pi
from numbers import Number


class TypeChecker:
    required_type = object

    def __init__(self, name=None):
        self.name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.required_type):
            raise TypeError(f'expecting a {self.required_type.__name__}')
        instance.__dict__[self.name] = value


def typechecked(**kwargs):
    def wrapper(cls):
        for name, value in kwargs.items():
            setattr(cls, name, value(name))
        return cls
    return wrapper


class NumberType(TypeChecker):
    required_type = Number


@typechecked(x=NumberType, y=NumberType)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'


class PointType(TypeChecker):
    required_type = Point


@typechecked(center=PointType, radius=NumberType)
class Circle:
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
from math import pi, sqrt


class TypeChecker:
    required_type = object

    def __init__(self, name, *, cast=True):
        self.name = name
        self.cast = cast

    def __get__(self, instance, cls):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.required_type):
            if self.cast:
                value = self.required_type(value)
            else:
                raise TypeError(f'expecting a {self.required_type.__name__}')
        instance.__dict__[self.name] = value


class IntType(TypeChecker):
    required_type = int


class FloatType(TypeChecker):
    required_type = float


class PositiveFloatType(FloatType):
    def __set__(self, instance, value):
        super().__set__(instance, value)
        if instance.__dict__[self.name] < 0:
            raise ValueError('expecting a non-negative float')


class Point:
    x = IntType('x', cast=False)
    y = IntType('y', cast=False)

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'


class PointType(TypeChecker):
    required_type = Point


class Circle:
    center = PointType('center')
    radius = PositiveFloatType('radius')

    def __init__(self, center, radius):
        self.radius = radius
        self.center = center

    @property
    def area(self):
        return pi * self.radius ** 2

    @area.setter
    def area(self, value):
        if value < 0:
            # What???
            raise ValueError('area cannot be negative')
        self.radius = sqrt(value / pi)

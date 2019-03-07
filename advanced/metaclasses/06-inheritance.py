# 06-inheritance.py
import inspect
from numbers import Number


class TypeChecker:
    required_type = object

    def __init__(self, name):
        self.ivar_name = f'_{name}'

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.ivar_name]

    def __set__(self, instance, value):
        # Beware: bool is a subclass of int (for historical reasons)
        if not isinstance(value, self.required_type) or \
                (self.required_type != bool and isinstance(value, bool)):
            raise TypeError(f'expecting a {self.required_type.__name__}')
        instance.__dict__[self.ivar_name] = value


class NumberType(TypeChecker):
    required_type = Number


class TypeChecked(type):
    def __new__(meta, name, bases, dct):
        # Add the name to the TypeChecker call
        for attr_name, value in dct.items():
            if inspect.isclass(value) and issubclass(value, TypeChecker):
                dct[attr_name] = value(attr_name)
        return super().__new__(meta, name, bases, dct)


class Typed(metaclass=TypeChecked):
    pass


class Point(Typed):
    x = NumberType
    y = NumberType

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'


class Point3D(Point):
    z = NumberType

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f'Point3D({self.x}, {self.y}, {self.z})'

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

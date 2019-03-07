# 00-meta_dataclasses.py
from dataclasses import dataclass
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


def typed_dataclass(cls):
    cls = dataclass(cls)

    for attr_name, attr_type in cls.__annotations__.items():
        class Checker(TypeChecker):
            required_type = attr_type

        setattr(cls, attr_name, Checker(attr_name))
    return cls


class TypeChecked(type):
    def __new__(meta, name, bases, dct):
        cls = super().__new__(meta, name, bases, dct)
        return typed_dataclass(cls)


class Typed(metaclass=TypeChecked):
    __annotations__ = {}


class Point(Typed):
    x: Number
    y: Number

    def __str__(self):
        return f'{self.x}, {self.y}'


class Point3D(Point):
    z: Number

    def __str__(self):
        return f'{self.x}, {self.y}, {self.z}'

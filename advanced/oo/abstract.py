"""
Illustrate the use of abstract base classes in Python.

The code below is conceptually equivalent to


class Shape:
    def move(self, dx, dy):
        raise NotImplementedError()

    def scale(self, dx, dy):
        raise NotImplementedError()

    @classmethod
    def foo(cls):
        raise NotImplementedError()
"""
import abc


class Shape(abc.ABC):
    @abc.abstractmethod
    def move(self, dx, dy):
        pass

    @abc.abstractmethod
    def scale(self, dx, dy):
        pass

    @abc.abstractclassmethod
    def foo(cls):
        pass

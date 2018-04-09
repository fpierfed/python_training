"""
Multiple inheritance and method resolution order

More info here https://www.python.org/download/releases/2.3/mro/

Note: super() is actually telling Python to walk the Class.__mro__ chain.
Note: MRO: 1. Check each child before its parents. 2. Check parents in order.
"""


class Person:
    def foo(self):
        print(f'Parent.foo()')

    def bar(self):
        print('Person.bar()')


class Child(Person):
    def bar(self):
        print('Child.bar()')
        super().bar()


class AnotherChild(Person):
    def bar(self):
        print('AnotherChild.bar()')
        super().bar()


class GrandSon(Child, AnotherChild):
    def bar(self):
        print('GrandSon.bar()')
        super().bar()


if __name__ == '__main__':
    gs = GrandSon()
    print('Class:', gs.__class__)
    print('MRO:', gs.__class__.__mro__)
    gs.bar()

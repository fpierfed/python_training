# 01-mixins.py
class Person:
    def foo(self):
        print(f'Person.foo')

    def bar(self):
        print('Person.bar')


class Child(Person):
    def bar(self, x):
        print('Child.bar')
        super().bar()       # <-- which args should we use here?


class AnotherChild(Person):
    def bar(self, x, y):
        print('AnotherChild.bar')
        super().bar()


class ChildMixIn:
    def bar(self, x):       # <-- simpler but not a silber bullet
        print('ChildMixIn.bar')
        super().bar(x)


class MIGrandSon(ChildMixIn, Child):
    def bar(self, x, y, z):
        print('GrandSon.bar')
        super().bar(x)


class GrandSon(Child, AnotherChild):
    def bar(self, x, y, z):
        print('GrandSon.bar')
        super().bar(x)

"""
Mixins are classes that are not part of any given class hierarchy  and do not
stand on their own.

They are useful to give extra functionality to a given class (and play well in
any hierarchy by calling super()).
"""
import random


def source(n=10):
    while n:
        yield random.randint(1, 10)
        n -= 1


class Echo:
    def __init__(self, source):
        for number in source:
            result = self.process(number)
            print(f'{number} -> {result}')

    def process(self, n):
        return n


class EchoPlusOne(Echo):
    def process(self, n):
        n = super().process(n)
        return n + 1


class EvenMixIn:
    def process(self, n):
        n = super().process(n)
        if not n % 2:
            return n


class EchoPlusOneEven(EvenMixIn, EchoPlusOne):
    pass


def format_mro(obj):
    return ' -> '.join([c.__name__ for c in obj.__class__.__mro__])


if __name__ == '__main__':
    print('Echo:')
    foo = Echo(source(5))
    print(f'{foo.__class__.__name__}.__mro__: {format_mro(foo)}\n')

    print('EchoPlusOne:')
    foo = EchoPlusOne(source(5))
    print(f'{foo.__class__.__name__}.__mro__: {format_mro(foo)}\n')

    print('EchoPlusOneEven:')
    foo = EchoPlusOneEven(source(5))
    print(f'{foo.__class__.__name__}.__mro__: {format_mro(foo)}\n')

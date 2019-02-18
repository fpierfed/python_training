# 00-gen.py
"""
Generators are the basis for iteration in Python

Three ways to create a generator:
 - Generator functions
 - Classes with __iter__ method
 - Generator expressions

Note: only class-based generators can be used more than once.
"""


# Generator function
def myrange(n):
    i = 0
    while i < n:
        yield i
        i += 1


# Class
class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        i = 0
        while i < self.n:
            yield i
            i += 1


# Generator expression
# myrange_exp = (x for x in range(n))

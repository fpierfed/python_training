class MyType(type):
    def __new__(meta, name, bases, methods):
        print(f'About to create a new {name} class')
        return super().__new__(meta, name, bases, methods)




class Point(metaclass=MyType):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x}, {self.y})'

    def __str__(self):
        return f'{self.x}, {self.y}'

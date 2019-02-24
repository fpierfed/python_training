# 04-log_meta.py
def logged(fn):
    def wrapper(*args, **kwargs):
        argstr = ', '.join([str(a) for a in args] +
                           [f'{k}={v}' for k, v in kwargs.items()])
        res = fn(*args, **kwargs)
        print(f'{fn.__name__}({argstr}) -> {res}')
        return res
    return wrapper


class LoggedType(type):
    def __init__(cls, name, bases, dct):
        for key, value in dct.items():
            if key in ('__str__', '__repr__'):
                # avoid infinite recursion due to the wrapper above.
                pass                            # leave as it
            elif callable(value):
                setattr(cls, key, logged(value))
        return super().__init__(name, bases, dct)


class Point(metaclass=LoggedType):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def __repr__(self):
        if 'x' in vars(self):
            # The class is already init-ed
            return f'Point({self.x}, {self.y})'
        else:
            # we are logging __init__(self, ...)
            #                         ^^^^
            return 'Point instance'

    def __str__(self):
        if 'x' in vars(self):
            # The class is already init-ed
            return f'{self.x}, {self.y}'
        else:
            # we are logging __init__(self, ...)
            #                         ^^^^
            return 'Point instance'

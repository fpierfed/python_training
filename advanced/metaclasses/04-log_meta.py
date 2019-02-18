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
    def __new__(meta, name, bases, dct):
        for name, value in dct.items():
            if callable(value):
                dct[name] = logged(value)
        return super().__new__(meta, name, bases, dct)


class Point(metaclass=LoggedType):
    # @logged                   <-- instread of this, we can use metaclasses
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # @logged
    def move(self, dx, dy):
        self.x += dx
        self.y += dy

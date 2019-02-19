# 00-getset.py
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, key):
        print(f'Getting {key}')
        return super().__getattribute__(key)

    def __delattr__(self, key):
        print(f'Deleting {key}')
        return super().__delattr__(key)

    def __setattr__(self, key, value):
        print(f'Setting {key}={value}')
        return super().__setattr__(key, value)

    def __getattr__(self, key):
        print(f'Attribute {key} is missing')
        return super().__getattr__(key)


if __name__ == '__main__':
    p = Point(1, 2)

    print()
    print(f'p.x = {p.x}')

    print()
    p.x = 99

    print()
    del(p.x)

    print()
    print(p.x)

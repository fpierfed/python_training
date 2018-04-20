from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

    def __post_init__(self):
        print('Any further customizaion goes here')


p = Point(1, 2)
print(f'str(p) = {p}')
print(f'repr(p) = {p!r}')

# iter_bonus.py
import dis


def simple():
    print('Hello')
    yield 42
    print('Good bye')
    yield 43


if __name__ == '__main__':
    print('Newly created generator')
    g = simple()

    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    print('First next() call')
    next(g)

    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    print('Second next() call')
    next(g)

    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    try:
        next(g)
    except StopIteration:
        print('Generator raised StopIteration exception')

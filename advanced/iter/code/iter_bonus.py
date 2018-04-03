import dis


def simple():
    print('Hello')
    yield 42
    print('Good bye')
    yield 43


if __name__ == '__main__':
    g = simple()
    print('Newly created generator')
    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    next(g)
    print('First next() call')
    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    next(g)
    print('Second next() call')
    print(f'Instruction pointer: {g.gi_frame.f_lasti}')
    dis.disco(g.gi_code, g.gi_frame.f_lasti)

    try:
        next(g)
    except StopIteration:
        print('Generator raised StopIteration exception')

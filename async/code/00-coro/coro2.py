# coro2.py
def foo():
    print('Hello')
    yield
    print('World')
    yield
    print('Bye')
    yield
    print('World')
    return 42


if __name__ == '__main__':
    g = foo()
    while True:
        try:
            next(g)
        except StopIteration as e:
            print(f'Coroutine returned {e.value}')
            break

# coro3.py
class Foo:
    def __iter__(self):
        print('Hello')
        yield
        print('World')
        yield
        print('Bye')
        yield
        print('World')
        return 42


if __name__ == '__main__':
    g = iter(Foo())
    while True:
        try:
            next(g)
        except StopIteration as e:
            print(f'Coroutine returned {e.value}')
            break

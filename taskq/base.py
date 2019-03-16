# base.py
def fib(n):
    if n < 0:
        raise Exception('fib(n) is undefined for n < 0')
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    N = 35
    REPETITIONS = 4

    for _ in range(REPETITIONS):
        res = fib(N)

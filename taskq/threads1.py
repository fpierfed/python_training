# threads1.py
import concurrent.futures as cf


def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('fib(n) is undefined for n < 0')
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    N = 35
    NUM_WORKERS = 4

    with cf.ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        results = pool.map(fib, [N, ] * NUM_WORKERS)

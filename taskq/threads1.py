# threads1.py
import concurrent.futures as cf
from base import fib


if __name__ == '__main__':
    N = 35
    NUM_WORKERS = 4

    with cf.ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        results = pool.map(fib, [N, ] * NUM_WORKERS)

# procs4_benchmark.py
from multiprocessing import Process
import sys
import time
import redis


def worker(inputq, outputq, n):
    conn = redis.StrictRedis('localhost')
    for _ in range(n):
        _, res = conn.blpop(inputq)
        conn.lpush(outputq, res)


if __name__ == '__main__':
    N = 10000
    try:
        NWORKERS = max(1, int(sys.argv[1]))
    except Exception:
        NWORKERS = 1

    tasks = 'tasks'
    results = 'results'

    for i in range(NWORKERS):
        Process(target=worker, args=(tasks, results, N // NWORKERS)).start()

    conn = redis.StrictRedis()

    t0 = time.time()
    with conn.pipeline() as pipe:
        for i in range(N):
            conn.lpush(tasks, 'foo')
        pipe.execute()

    received = 0
    while received < N:
        res = conn.lpop(results)
        if res is not None:
            received += 1
    dt = time.time() - t0
    print(f'{NWORKERS} workers: {N / dt:.02f} jobs/s')

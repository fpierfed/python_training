# procs4.py
import multiprocessing as mp
import json
import redis
from base import fib


def worker(inputq, outputq):
    conn = redis.StrictRedis('localhost')

    while True:
        _, raw_work = conn.blpop(inputq)
        work = json.loads(raw_work)
        if work is None:
            break

        fname, args = work
        fn = globals()[fname]
        res = fn(*args)
        conn.lpush(outputq, json.dumps(res))


if __name__ == '__main__':
    N = 35
    NUM_WORKERS = 4

    tasks = 'tasks'
    results = 'results'

    conn = redis.StrictRedis()
    for i in range(NUM_WORKERS):
        conn.lpush(tasks, json.dumps(('fib', (N, ))))

    for i in range(NUM_WORKERS):
        mp.Process(target=worker, args=(tasks, results)).start()

    for i in range(NUM_WORKERS):
        json.loads(conn.blpop(results)[1])

    for i in range(NUM_WORKERS):
        conn.lpush(tasks, json.dumps(None))

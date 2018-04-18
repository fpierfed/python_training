import multiprocessing as mp
import json
import redis


def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('fib(n) is undefined for n < 0')
    return fib(n - 1) + fib(n - 2)


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

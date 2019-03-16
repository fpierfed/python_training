# procs5_consumer.py
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
    NUM_WORKERS = 4

    tasks = 'tasks'
    results = 'results'

    for i in range(NUM_WORKERS):
        mp.Process(target=worker, args=(tasks, results)).start()

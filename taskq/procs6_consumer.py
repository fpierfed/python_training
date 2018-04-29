# procs6_consumer.py
import multiprocessing as mp
import json
import uuid
import redis


REDIS_HOST = 'localhost'


def fib(n):
    if n <= 2:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise Exception('fib(n) is undefined for n < 0')
    return fib(n - 1) + fib(n - 2)


def worker(inputq, outputq):
    _id = str(uuid.uuid4())
    conn = redis.StrictRedis(REDIS_HOST)

    while True:
        _, raw_work = conn.blpop(inputq)
        work = json.loads(raw_work)

        fname, args = work
        fn = globals()[fname]

        argstr = ', '.join([str(a) for a in args])
        print(f'Worker {_id}: got request for {fname}({argstr})')
        res = fn(*args)
        conn.lpush(outputq, json.dumps((_id, res)))


if __name__ == '__main__':
    NUM_WORKERS = 4

    tasks = 'tasks'
    results = 'results'

    for i in range(NUM_WORKERS):
        mp.Process(target=worker, args=(tasks, results)).start()

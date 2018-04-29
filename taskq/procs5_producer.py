# procs5_producer.py
import json
import redis


if __name__ == '__main__':
    N = 35
    NUM_WORKERS = 4

    tasks = 'tasks'
    results = 'results'

    conn = redis.StrictRedis()
    for i in range(NUM_WORKERS):
        conn.lpush(tasks, json.dumps(('fib', (N, ))))

    for i in range(NUM_WORKERS):
        json.loads(conn.blpop(results)[1])

    for i in range(NUM_WORKERS):
        conn.lpush(tasks, json.dumps(None))

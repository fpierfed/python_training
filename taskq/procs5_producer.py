import json
import redis


if __name__ == '__main__':
    N = 35
    NUM_TASKS = 8
    REDIS_HOST = 'localhost'

    tasks = 'tasks'
    results = 'results'

    conn = redis.StrictRedis(REDIS_HOST)
    for i in range(NUM_TASKS):
        conn.lpush(tasks, json.dumps(('fib', (N, ))))

    for i in range(NUM_TASKS):
        json.loads(conn.blpop(results)[1])

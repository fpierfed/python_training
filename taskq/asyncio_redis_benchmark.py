import asyncio
import time
import aioredis as redis
import uvloop


async def worker(inputq, outputq, n):
    conn = await redis.create_redis('redis://localhost')
    for _ in range(n):
        res = None
        while res is None:
            res = await conn.lpop(inputq)
        await conn.lpush(outputq, res)


async def producer(inputq, outputq, n):
    conn = await redis.create_redis('redis://localhost')

    t0 = time.time()
    for _ in range(N):
        await conn.lpush(outputq, b'foo')

    received = 0
    while received < N:
        res = await conn.lpop(inputq)
        if res is not None:
            received += 1
    dt = time.time() - t0
    print(f'{NWORKERS} workers: {N / dt:.02f} jobs/s')


if __name__ == '__main__':
    N = 10000
    NWORKERS = 2

    tasks = b'tasks'
    results = b'results'

    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    loop = asyncio.get_event_loop()

    for i in range(NWORKERS):
        asyncio.ensure_future(worker(tasks, results, N // NWORKERS), loop=loop)

    loop.run_until_complete(producer(results, tasks, N))

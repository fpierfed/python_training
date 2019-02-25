# procs3_benchmark.py
from multiprocessing import Process
import time
from procs3_queue import QueueManager


def work(n):
    manager = QueueManager(address=('localhost', 9999), authkey=b'foo')
    manager.connect()

    inq = manager.get_taskq()
    outq = manager.get_resultq()
    for _ in range(n):
        outq.put(inq.get())


if __name__ == '__main__':
    N = 10000
    NWORKERS = 2

    manager = QueueManager(address=('localhost', 9999), authkey=b'foo')
    manager.connect()
    tasks = manager.get_taskq()
    results = manager.get_resultq()

    for _ in range(NWORKERS):
        Process(target=work, args=(N // NWORKERS, )).start()

    t0 = time.time()
    for _ in range(N):
        tasks.put(None)
    for _ in range(N):
        results.get()
    dt = time.time() - t0
    print(f'{NWORKERS} workers: {N / dt:.02f} jobs/s')

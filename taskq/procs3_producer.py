# # procs3_producer.py
from procs3_queue import QueueManager
from base import fib


manager = QueueManager(address=('localhost', 9999), authkey=b'foo')
manager.connect()
tasks = manager.get_taskq()
results = manager.get_resultq()

N = 35
NUM_WORKERS = 4

for i in range(NUM_WORKERS):
    tasks.put((fib, (N, )))

for i in range(NUM_WORKERS):
    results.get()

for i in range(NUM_WORKERS):
    tasks.put(None)

# procs3_consumer.py
from multiprocessing import Process
from procs2 import worker
from procs3_queue import QueueManager


manager = QueueManager(address=('localhost', 9999), authkey=b'foo')
manager.connect()
inputq = manager.get_taskq()
outputq = manager.get_resultq()

NUM_WORKERS = 4

procs = []
for i in range(NUM_WORKERS):
    p = Process(target=worker, args=(inputq, outputq))
    p.start()
    procs.append(p)

# Wait for the processes to finish their work!!!!!
for p in procs:
    p.join()

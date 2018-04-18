from multiprocessing import managers
from queue import Queue


tasks = Queue()
results = Queue()


class QueueManager(managers.BaseManager):
    pass


QueueManager.register('get_taskq', callable=lambda: tasks)
QueueManager.register('get_resultq', callable=lambda: results)


if __name__ == '__main__':
    manager = QueueManager(address=('', 9999), authkey=b'foo')
    server = manager.get_server()
    server.serve_forever()

# loop5.py
import time


class Task:
    _all_tasks = set()

    def __init__(self, coroutine):
        Task._all_tasks.add(self)
        self.id = len(Task._all_tasks)

        self._coroutine = coroutine
        self._callbacks = []

        self.result = None
        self.exception = None
        self.done = False

    def __next__(self):
        return self._coroutine.__next__()

    @classmethod
    def all_tasks(cls):
        return cls._all_tasks

    def add_done_callback(self, callback):
        if callable(callback):
            self._callbacks.append(callback)
        else:
            raise TypeError('Expecting a callable')

    def remove_done_callback(self, callback):
        self._callbacks.remove(callback)

    @property
    def done_callbacks(self):
        return self._callbacks

    @property
    def result(self):
        return self._result

    @result.setter
    def result(self, value):
        self.done = True
        self._result = value

    @property
    def exception(self):
        return self._exception

    @exception.setter
    def exception(self, value):
        self.done = True
        self._exception = value


def coro(name, n=10):
    i = 0
    while i < n:
        print(f'{name}: {i}')
        i += 1
        yield
    return n


def fail(n=10):
    i = 0
    while i < n:
        print('fail:', i)
        yield
        i += 1
    raise Exception('Done')


def blocking():
    yield
    print('blocking')
    time.sleep(5)


def mycallback(task):
    if task.exception:
        print(f'Task {task.id} raised {task.exception!r}')
    else:
        print(f'Task {task.id} result: {task.result}')


if __name__ == '__main__':
    tasks = [
        Task(coro('foo')),
        Task(coro('bar', n=7)),
        Task(fail(n=3)),
        Task(blocking())
    ]
    for task in tasks:
        task.add_done_callback(mycallback)

    while tasks:
        current = tasks.pop(0)
        try:
            next(current)
        except StopIteration as e:
            current.result = e.value
        except Exception as e:
            current.exception = e
        else:
            tasks.append(current)
        finally:
            if current.done:
                for callback in current.done_callbacks:
                    callback(current)
    print('All done')

    # What are the problems with this simple event loop?
    # - NEW: what is the role of callbacks?
    # - NEW: what about exceptions?
    # - NEW: how can we spawn a coroutine from e.g., a callback?
    # - 100% CPU usage
    # - Is round-robing the best scheduling?
    # - What about IO events (e.g., sockets)?
    # - Others?

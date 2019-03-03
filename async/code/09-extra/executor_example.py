# executor_example.py
"""
Show how to run blocking functions in a separate thread of process.
"""
import asyncio
import concurrent.futures as cf
import time


def long_running_function(n):
    """Sleep for n seconds."""
    time.sleep(n)


def high_cpu_function(n):
    """Burn CPU cycles for n seconds."""
    while n:
        n -= 1


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    # BAD!
    # loop.run_until_complete(asyncio.wait([
    #     long_running_function(10),
    #     long_running_function(10),
    #     high_cpu_function(245000000),
    #     high_cpu_function(245000000),
    # ]))

    # Better
    # executor = cf.ThreadPoolExecutor()
    # loop.run_until_complete(asyncio.wait([
    #     loop.run_in_executor(executor, long_running_function, 10),
    #     loop.run_in_executor(executor, long_running_function, 10),
    #     loop.run_in_executor(executor, high_cpu_function, 245000000),
    #     loop.run_in_executor(executor, high_cpu_function, 245000000),
    # ]))

    # Best?
    executor = cf.ProcessPoolExecutor()
    loop.run_until_complete(asyncio.wait([
        loop.run_in_executor(executor, long_running_function, 10),
        loop.run_in_executor(executor, long_running_function, 10),
        loop.run_in_executor(executor, high_cpu_function, 245000000),
        loop.run_in_executor(executor, high_cpu_function, 245000000),
    ]))

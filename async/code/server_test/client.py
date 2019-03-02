# client.py
import concurrent.futures as cf
import socket
import sys
import time


def client(address, n):
    host, port = address

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    for i in range(n):
        s.send(b'Hello')
        s.recv(10000)


if __name__ == '__main__':
    try:
        NUM_WORKERS = max(1, int(sys.argv[1]))
    except Exception:
        NUM_WORKERS = 1

    N = 50000
    t0 = time.time()

    with cf.ThreadPoolExecutor(max_workers=NUM_WORKERS) as pool:
        futs = [pool.submit(client, ('localhost', 9999), N)
                for _ in range(NUM_WORKERS)]
        cf.wait(futs, timeout=None, return_when=cf.ALL_COMPLETED)

    dt = time.time() - t0
    print(f'{NUM_WORKERS} client(s): {N * NUM_WORKERS / dt:.02f} roundtrip/s')

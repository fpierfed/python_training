# 02-server_thread.py
import argparse
import socket
from threading import Thread


class Server:
    def __init__(self, address):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(address)
        self.sock.listen(5)
        print(f'Listening on {":".join([str(x) for x in address])}')

    def serve_forever(self):
        while True:
            client, addr = self.sock.accept()
            print(f'Client connected from {addr}')
            # Thread(target=connection_handler, args=(client, )).start()
            self.handle_connection(client)

    def handle_connection(self, client):
        while True:
            data = client.recv(10000)
            if not data:
                break
            client.sendall(data)
        print('Connection closed')
        client.close()


class ThreadingMixIn:
    def handle_connection(self, client):
        Thread(target=super().handle_connection, args=(client, )).start()


class ThreadingServer(ThreadingMixIn, Server):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', type=str, choices=('standard', 'threaded'),
                        nargs='?', default='standard')
    args = parser.parse_args()

    print(f'Mode: {args.mode}')
    if args.mode == 'threaded':
        server = ThreadingServer(('localhost', 9999))
    else:
        server = Server(('localhost', 9999))

    server.serve_forever()

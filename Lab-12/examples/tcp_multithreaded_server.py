#!/usr/bin/env python
import socket, sys, threading


class ClientThread(threading.Thread):
    def __init__(self, connection):
        threading.Thread.__init__(self)
        # ...

    def run(self):
        # obsluga odbierania i wysylania danych
        pass


class Server:
    def __init__(self, ip, port):
        # ...
        pass

    def run(self):
        try:
            # socket, bind, listen

            while True:
                # accept

                c = ClientThread(connection)
                c.start()

        except socket.error, e:
            # ...
            pass


if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()
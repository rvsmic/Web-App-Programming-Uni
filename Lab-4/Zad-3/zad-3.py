import socket

HOST = '127.0.0.1'
PORT = 20202

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)
    print(f"Received data from {address}: {data.decode()}")
    server_socket.sendto(data, address)
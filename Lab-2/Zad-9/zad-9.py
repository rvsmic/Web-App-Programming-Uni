import socket

server_address = ('127.0.0.1', 2906)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
    ip_address = '127.0.0.1'
    client_socket.sendto(ip_address.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    hostname = data.decode()
    print(f'Otrzymana nazwa hosta: {hostname}')

finally:
    client_socket.close()
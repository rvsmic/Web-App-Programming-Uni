import socket

def get_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        return "Unknown"

HOST = '127.0.0.1'
PORT = 20202

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)
    hostname = data.decode()
    print(f"Odebrany hostname od {address}: {hostname}")

    ip = get_ip(hostname)

    server_socket.sendto(ip.encode(), address)

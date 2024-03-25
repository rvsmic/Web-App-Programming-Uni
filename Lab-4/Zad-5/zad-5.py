import socket

def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
        return hostname
    except socket.herror:
        return "Unknown"

HOST = '127.0.0.1'
PORT = 20202

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)
    ip = data.decode()
    print(f"Odebrany adres ip od {address}: {ip}")

    hostname = get_hostname(ip)

    server_socket.sendto(hostname.encode(), address)

import socket

def calculate(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

import socket

HOST = '127.0.0.1'
PORT = 20202

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))
print(f"Serwer nasłuchuje na {HOST}:{PORT}")

while True:
    data, address = server_socket.recvfrom(1024)
    data = data.decode()
    print(f"Received data from {address}: {data}")

    num1, operator, num2 = data.split()

    num1 = int(num1)
    num2 = int(num2)

    result = calculate(num1, operator, num2)

    server_socket.sendto(str(result).encode(), address)
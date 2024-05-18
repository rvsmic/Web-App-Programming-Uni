import socket

HOST = 'httpbin.org'
PORT = 80
PATH = '/image/png'

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    request = f"GET {PATH} HTTP/1.1\r\nHost: {HOST}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())

    response = b""
    while True:
        data = s.recv(4096)
        if not data:
            break
        response += data

header_data, image_data = response.split(b'\r\n\r\n', 1)

with open('obrazek.png', 'wb') as f:
    f.write(image_data)

print("Pobrano obrazek")

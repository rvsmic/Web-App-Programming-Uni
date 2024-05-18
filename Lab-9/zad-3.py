import socket

# serwer nie działa więc korzystam z poprzedniego zadania
HOST = 'httpbin.org'
PORT = 80
PATH = '/image/png'

def get_headers():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        request = (
            f"HEAD {PATH} HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            f"Connection: close\r\n\r\n"
        )
        s.sendall(request.encode())
        
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    
    header_data = response.decode()
    return header_data

def get_image_part(start, end):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        
        request = (
            f"GET {PATH} HTTP/1.1\r\n"
            f"Host: {HOST}\r\n"
            f"Range: bytes={start}-{end}\r\n"
            f"Connection: close\r\n\r\n"
        )
        s.sendall(request.encode())
        
        response = b""
        while True:
            data = s.recv(4096)
            if not data:
                break
            response += data
    
    header_data, image_data = response.split(b'\r\n\r\n', 1)
    return image_data

headers = get_headers()

content_length = 0
for line in headers.split('\r\n'):
    if line.lower().startswith('content-length:'):
        content_length = int(line.split(':')[1].strip())
        break

part_size = content_length // 3
parts = [
    (0, part_size - 1),
    (part_size, 2 * part_size - 1),
    (2 * part_size, content_length - 1)
]

image_parts = [get_image_part(start, end) for start, end in parts]

full_image = b''.join(image_parts)

with open('obrazek.png', 'wb') as f:
    f.write(full_image)

print("Pobrano obrazek w 3 częściach")

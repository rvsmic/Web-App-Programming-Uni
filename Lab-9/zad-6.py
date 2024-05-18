import socket

# Serwer nie działa więc korzystam z poprzedniego zadania
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

def get_last_modified_date():
    headers = get_headers()
    for line in headers.split('\r\n'):
        if line.lower().startswith('last-modified:'):
            return line.split(':', 1)[1].strip()
    return None

def save_last_modified_date(date):
    with open('last_modified.txt', 'w') as f:
        f.write(date)

def load_last_modified_date():
    try:
        with open('last_modified.txt', 'r') as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

current_last_modified = get_last_modified_date()
if current_last_modified is None:
    print("Serwer nie obsługuje nagłówka Last-Modified.")
else:
    last_saved_modified = load_last_modified_date()
    if current_last_modified == last_saved_modified:
        print("Obrazek się nie zmienił. Nie pobieram ponownie.")
    else:
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

        save_last_modified_date(current_last_modified)
        print("Pobrano nowy obrazek i zapisano datę ostatniej modyfikacji.")


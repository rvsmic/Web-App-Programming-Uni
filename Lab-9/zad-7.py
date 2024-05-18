import socket

def handle_request(client_socket):
    request_data = client_socket.recv(1024).decode()
    request_lines = request_data.split('\r\n')
    request_method, request_path, _ = request_lines[0].split(' ')

    if request_method == 'GET':
        if request_path == '/':
            response_body = '<h1>Strona główna</h1>'
            response_status = '200 OK'
        else:
            response_body = '<h1>404 - Nie znaleziono strony</h1>'
            response_status = '404 Not Found'
    else:
        response_body = '<h1>Metoda nieobsługiwana</h1>'
        response_status = '405 Method Not Allowed'

    response_headers = [
        'HTTP/1.1 ' + response_status,
        'Content-Type: text/html',
        'Content-Length: ' + str(len(response_body)),
        'Connection: close'
    ]
    response = '\r\n'.join(response_headers) + '\r\n\r\n' + response_body

    client_socket.sendall(response.encode())
    client_socket.close()

def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f'Serwer działa na {host}:{port}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Klient podłączony: {client_address[0]}:{client_address[1]}')
        handle_request(client_socket)

if __name__ == '__main__':
    host = '127.0.0.1'
    port = 8080
    run_server(host, port)
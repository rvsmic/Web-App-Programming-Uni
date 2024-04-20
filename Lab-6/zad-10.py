import socket

HOST = '127.0.0.1'
PORT = 8025

GREETING = b'220 localhost SMTP server ready\r\n'
OK_RESPONSE = b'250 OK\r\n'
UNKNOWN_COMMAND_RESPONSE = b'500 Unknown command\r\n'

def handle_client(client_socket):
    client_socket.sendall(GREETING)

    while True:
        data = client_socket.recv(1024)
        if not data:
            break

        command = data.decode().strip().upper()

        if command == 'HELO':
            client_socket.sendall(OK_RESPONSE)
        elif command == 'MAIL FROM':
            client_socket.sendall(OK_RESPONSE)
        elif command == 'RCPT TO':
            client_socket.sendall(OK_RESPONSE)
        elif command == 'DATA':
            client_socket.sendall(OK_RESPONSE)
            while True:
                message_data = client_socket.recv(1024)
                if message_data == b'\r\n.\r\n':
                    break
            client_socket.sendall(OK_RESPONSE)
        elif command == 'QUIT':
            client_socket.sendall(b'221 Bye\r\n')
            break
        else:
            client_socket.sendall(UNKNOWN_COMMAND_RESPONSE)

    client_socket.close()

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)

    print(f'Server listening on {HOST}:{PORT}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Client connected: {client_address[0]}:{client_address[1]}')
        handle_client(client_socket)

    server_socket.close()

if __name__ == '__main__':
    run_server()
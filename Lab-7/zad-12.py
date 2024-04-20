import socket

# Adres i port serwera
HOST = '127.0.0.1'
PORT = 11000
USER = 'michal'
PASSWORD = 'password'

# Komendy obsługiwane przez serwer
COMMANDS = ['USER', 'PASS', 'LIST', 'RETR', 'QUIT']

# Symulowane wiadomości e-mail
MESSAGES = [
    'From: sender@example.com',
    'To: recipient@example.com',
    'Subject: Hello',
    '',
    'This is a test email.',
    'End of message.'
]

def handle_client(client_socket):
    logged_in = False
    client_socket.send(b'+OK POP3 server ready\r\n')

    while True:
        data = client_socket.recv(1024).decode().strip()
        if not data:
            break

        command = data.split(' ')[0].upper()
        if command not in COMMANDS:
            client_socket.send(b'-ERR Command not implemented\r\n')
            continue

        if command == 'USER':
            if data.split(' ')[1] != USER:
                client_socket.send(b'-ERR Authentication failed\r\n')
            else:
                client_socket.send(b'+OK\r\n')
        elif command == 'PASS':
            if data.split(' ')[1] != PASSWORD:
                client_socket.send(b'-ERR Authentication failed\r\n')
            else:
                logged_in = True
                client_socket.send(b'+OK Logged in.\r\n')
        elif command == 'STAT':
            if logged_in:
                client_socket.send(b'+OK 1 100\r\n')
            else:
                client_socket.send(b'-ERR Authentication required\r\n')
        elif command == 'LIST':
            if logged_in:
                client_socket.send(b'+OK 1 message:\r\n')
                client_socket.send(b'+OK 1 100\r\n')
            else:
                client_socket.send(b'-ERR Authentication required\r\n')
        elif command == 'DELE':
            if logged_in:
                try:
                    message_number = int(data.split(' ')[1])
                    if message_number < 1 or message_number > len(MESSAGES):
                        client_socket.send(b'-ERR No such message\r\n')
                    else:
                        client_socket.send(b'+OK Marked to be deleted.\r\n')
                except IndexError:
                    client_socket.send(b'-ERR Invalid message number\r\n')
                except ValueError:
                    client_socket.send(b'-ERR Invalid message number\r\n')
            else:
                client_socket.send(b'-ERR Authentication required\r\n')
        elif command.startswith('RETR'):
            if logged_in:
                try:
                    message_number = int(data.split(' ')[1])
                    if message_number < 1 or message_number > len(MESSAGES):
                        client_socket.send(b'-ERR No such message\r\n')
                    else:
                        client_socket.send(b'+OK\r\n')
                        for line in MESSAGES[message_number - 1].split('\n'):
                            client_socket.send(line.encode() + b'\r\n')
                        client_socket.send(b'.\r\n')
                except IndexError:
                    client_socket.send(b'-ERR Invalid message number\r\n')
                except ValueError:
                    client_socket.send(b'-ERR Invalid message number\r\n')
            else:
                client_socket.send(b'-ERR Authentication required\r\n')
        elif command == 'QUIT':
            logged_in = False
            client_socket.send(b'+OK POP3 server signing off\r\n')
            break

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
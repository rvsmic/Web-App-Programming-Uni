import socket

HOST = '127.0.0.1'
PORT = 1433

COMMANDS = ['LOGIN', 'LIST', 'FETCH', 'LOGOUT']

def handle_command(command, is_logged_in):
    if command.startswith('LOGIN'):
        if is_logged_in:
            return 'NO Already logged in\n'
        else:
            try:
                username, password = command.split()[1:]
            except ValueError:
                return 'NO Invalid username or password\n'
            if username == 'michal@wp.pl' and password == 'pass':
                return 'OK LOGIN successful\n'
            else:
                return 'NO Invalid username or password\n'
    elif command.startswith('SELECT'):
        if not is_logged_in:
            return 'NO Please login first\n'
        else:
            return 'OK SELECT successful\n'
    elif command.startswith('LIST'):
        if not is_logged_in:
            return 'NO Please login first\n'
        else:
            return 'OK 1 EXISTS\n1 1\n'
    elif command.startswith('FETCH'):
        if not is_logged_in:
            return 'NO Please login first\n'
        else:
            message_id = command.split()[1]
            if message_id == '1':
                return 'OK 1 FETCH (BODY[TEXT] "Message 1 content")\n'
            elif message_id == '2':
                return 'OK 2 FETCH (BODY[TEXT] "Message 2 content")\n'
            else:
                return 'NO Invalid message ID\n'
    elif command.startswith('LOGOUT'):
        if not is_logged_in:
            return 'NO Please login first\n'
        else:
            return 'OK Goodbye\n'
    else:
        return 'NO Unknown command\n'

def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)
    print(f'Server listening on {HOST}:{PORT}')

    while True:
        client_socket, client_address = server_socket.accept()
        print(f'Connected to client {client_address}')

        is_logged_in = False

        while True:
            data = client_socket.recv(1024).decode()
            if not data:
                break
            response = handle_command(data, is_logged_in)
            client_socket.sendall(response.encode())

            if response.startswith('OK LOGIN'):
                is_logged_in = True
            elif response.startswith('OK Goodbye') or data.startswith('QUIT'):
                is_logged_in = False
                break
            
        client_socket.close()
        print(f'Connection closed with client {client_address}')
    server_socket.close()

run_server()

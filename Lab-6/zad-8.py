import socket
import base64

def send_email():
    server_address = 'dsmka.wintertoad.xyz'
    server_port = 587

    sender = input("Podaj adres nadawcy: ")
    recipient = input("Podaj adres odbiorcy: ")
    subject = input("Podaj temat wiadomości: ")

    attachment_path = input("Podaj ścieżkę do załącznika: ")
    attachment_name = input("Podaj nazwę załącznika: ")

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client_socket.connect((server_address, server_port))

        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(b'EHLO michal\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(b'AUTH LOGIN\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        username = base64.b64encode(input("Podaj login: ").encode()).decode()
        client_socket.sendall(username.encode() + b'\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        password = base64.b64encode(input("Podaj hasło: ").encode()).decode()
        client_socket.sendall(password.encode() + b'\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(f'MAIL FROM: <{sender}>\r\n'.encode())
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(f'RCPT TO: <{recipient}>\r\n'.encode())
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(b'DATA\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

        client_socket.sendall(f'From: {sender}\r\n'.encode())
        client_socket.sendall(f'To: {recipient}\r\n'.encode())
        client_socket.sendall(f'Subject: {subject}\r\n'.encode())

        client_socket.sendall(f'Content-Type: image/jpeg; name={attachment_name}\r\n'.encode())
        client_socket.sendall(b'Content-Disposition: attachment\r\n')
        client_socket.sendall(b'\r\n')

        with open(attachment_path, 'rb') as attachment_file:
            attachment_data = attachment_file.read()
            client_socket.sendall(attachment_data)

        client_socket.sendall(b'.\r\n')
        
        client_socket.sendall(b'QUIT\r\n')
        response = client_socket.recv(1024).decode()
        print(response)

    finally:
        client_socket.close()

send_email()
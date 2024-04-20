import socket
import base64

def send_email(login, password, sender, recipients, subject, attachment_path):
    server_address = 'dsmka.wintertoad.xyz'
    server_port = 587
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    response = client_socket.recv(1024).decode()
    print(response)

    ehlo_command = 'EHLO michal\r\n'
    client_socket.send(ehlo_command.encode())
    response = client_socket.recv(1024).decode()
    print(response)

    auth_login_command = 'AUTH LOGIN\r\n'
    client_socket.write(auth_login_command.encode())
    response = client_socket.read(1024).decode()
    print(response)

    username = base64.b64encode(login.encode()).decode() + '\r\n'
    client_socket.write(username.encode())
    response = client_socket.read(1024).decode()
    print(response)

    passw = base64.b64encode(password.encode()).decode() + '\r\n'
    client_socket.write(passw.encode())
    response = client_socket.read(1024).decode()
    print(response)

    mail_from_command = 'MAIL FROM: <' + sender + '>\r\n'
    client_socket.write(mail_from_command.encode())
    response = client_socket.read(1024).decode()
    print(response)

    for recipient in recipients:
        rcpt_to_command = 'RCPT TO: <' + recipient + '>\r\n'
        client_socket.write(rcpt_to_command.encode())
        response = client_socket.read(1024).decode()
        print(response)

    data_command = 'DATA\r\n'
    client_socket.write(data_command.encode())
    response = client_socket.read(1024).decode()
    print(response)

    message_header = 'From: ' + sender + '\r\n'
    message_header += 'To: ' + ', '.join(recipients) + '\r\n'
    message_header += 'Subject: ' + subject + '\r\n'
    client_socket.write(message_header.encode())

    attachment = 'Content-Disposition: attachment; filename=' + attachment_path + '\r\n\r\n'
    with open(attachment_path, 'rb') as file:
        attachment += file.read().decode() + '\r\n\r\n'
    client_socket.write(attachment.encode())

    end_of_message = '.\r\n'
    client_socket.write(end_of_message.encode())
    response = client_socket.read(1024).decode()
    print(response)

    quit_command = 'QUIT\r\n'
    client_socket.write(quit_command.encode())
    response = client_socket.read(1024).decode()
    print(response)
    client_socket.close()

sender = input('Podaj adres nadawcy: ')
login = input('Podaj login: ')
password = input('Podaj hasło: ')
recipients = input('Podaj adresy odbiorców (oddzielone przecinkami): ').split(',')
subject = input('Podaj temat wiadomości: ')
attachment_path = input('Podaj ścieżkę do załącznika: ')

send_email(login, password, sender, recipients, subject, attachment_path)
import poplib

pop3_server = 'dsmka.wintertoad.xyz'
pop3_port = 110
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

pop3_connection = poplib.POP3(pop3_server, pop3_port)
pop3_connection.user(username)
pop3_connection.pass_(password)

message_count, mailbox_size = pop3_connection.stat()
print(f"Liczba wiadomości: {message_count}")
print(f"Rozmiar skrzynki: {mailbox_size} bajtów")

for i in range(1, message_count + 1):
    response = pop3_connection.retr(i)
    message_lines = response[1]
    message_size = sum(len(line) for line in message_lines)
    print(f"Wiadomość {i}: {message_size} bajtów")

pop3_connection.quit()
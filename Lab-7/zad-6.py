import poplib

pop3_server = 'dsmka.wintertoad.xyz'
pop3_port = 110
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

pop3_connection = poplib.POP3(pop3_server, pop3_port)
pop3_connection.user(username)
pop3_connection.pass_(password)

num_messages = len(pop3_connection.list()[1])
print(f"Ilość wiadomości w skrzynce: {num_messages}")

pop3_connection.quit()
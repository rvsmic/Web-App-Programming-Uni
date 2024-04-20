import poplib

pop3_server = 'dsmka.wintertoad.xyz'
pop3_port = 110
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

def get_total_message_size():
    pop3_connection = poplib.POP3(pop3_server, pop3_port)
    pop3_connection.user(username)
    pop3_connection.pass_(password)

    _, total_size = pop3_connection.stat()

    pop3_connection.quit()

    return total_size

total_size = get_total_message_size()
print(f"Suma rozmiarów wiadomości: {total_size} bajtów")

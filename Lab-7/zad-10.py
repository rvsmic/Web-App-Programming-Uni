import poplib

pop3_server = 'dsmka.wintertoad.xyz'
pop3_port = 110
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

pop3 = poplib.POP3(pop3_server, pop3_port)

# Logowanie
pop3.user(username)
pop3.pass_(password)

num_messages = len(pop3.list()[1])
print(f"Liczba wiadomości w skrzynce: {num_messages}")

for i in range(1, num_messages + 1):
    response, lines, octets = pop3.retr(i)
    message = b"\n".join(lines).decode("utf-8")
    print(f"\nWiadomość {i}:\n{message}")

pop3.quit()
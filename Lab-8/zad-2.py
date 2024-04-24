import imaplib

imap_server = 'dsmka.wintertoad.xyz'
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

imap = imaplib.IMAP4(imap_server)
imap.login(username, password)
imap.select('Inbox')

status, response = imap.status('Inbox', '(MESSAGES)')

if status == 'OK':
    messages_count = int(response[0].decode().split()[2][0])
    print(f"Liczba wiadomości w skrzynce Inbox: {messages_count}")
else:
    print("Błąd podczas pobierania informacji o skrzynce odbiorczej")
imap.logout()
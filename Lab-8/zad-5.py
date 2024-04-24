import imaplib

imap_server = 'dsmka.wintertoad.xyz'
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

MESSAGE_NUMBER = 123

imap = imaplib.IMAP4(imap_server)
imap.login(username, password)
imap.select('INBOX')

status, response = imap.search(None, 'ALL')
numbers = list(map(lambda x: x.decode(), response[0].split()))
for num in response[0].split():
    status, data = imap.fetch(num, '(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])')
    if status == 'OK':
        print('--- Wiadomość', num.decode(), '---')
        print(data[0][1].decode().strip())
        print('-------------------')

print('--- Usuwanie wiadomości ---')
msg_num = input('Podaj numer wiadomości do usunięcia: ')
if msg_num in numbers:
    imap.store(msg_num, '+FLAGS', '\\Deleted')
    imap.expunge()
    print(f'Wiadomość {msg_num} usunięta')

imap.logout()
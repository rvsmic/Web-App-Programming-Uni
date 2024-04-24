import imaplib

imap_server = 'dsmka.wintertoad.xyz'
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

imap = imaplib.IMAP4(imap_server)
imap.login(username, password)
imap.select('INBOX')
status, response = imap.search(None, 'UNSEEN')

if status == 'OK':
    no_unseen = True
    for num in response[0].split():
        no_unseen = False
        status, data = imap.fetch(num, '(RFC822)')
        if status == 'OK':
            print('--- Wiadomość', num.decode(), '---')
            print(data[0][1].decode())
            print('-------------------------')

            imap.store(num, '+FLAGS', '\\Seen')
            print('Oznaczono jako przeczytane')
    if no_unseen:
        print('Brak nieprzeczytanych wiadomości')

imap.close()
imap.logout()
import imaplib

imap_server = 'dsmka.wintertoad.xyz'
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

def count_total_messages():
    imap = imaplib.IMAP4(imap_server)
    imap.login(username, password)

    status, mailbox_list = imap.list()

    total_messages = 0
    mailbox_list = list(map(lambda x: x.decode().split('.')[1].strip('"').strip(' '), mailbox_list))

    for mailbox in mailbox_list:
        imap.select(mailbox)

        status, message_count = imap.search(None, 'ALL')
        message_count = len(message_count[0].split())

        total_messages += message_count

    print(f"Liczba wiadomości we wszystkich skrzynkach: {total_messages}")

    imap.logout()

count_total_messages()
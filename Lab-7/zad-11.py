import poplib
import email

pop3_server = 'dsmka.wintertoad.xyz'
pop3_port = 110
username = 'test1@wintertoad.xyz'
password = 'P@ssw0rd'

pop3_conn = poplib.POP3(pop3_server, pop3_port)
pop3_conn.user(username)
pop3_conn.pass_(password)

num_messages = len(pop3_conn.list()[1])
response, message_lines, octets = pop3_conn.retr(num_messages)

message_content = b'\r\n'.join(message_lines).decode('utf-8')

message = email.message_from_string(message_content)

for part in message.walk():
    if part.get_content_maintype() == 'multipart':
        continue
    if part.get('Content-Disposition') is None:
        continue

    if part.get_content_type() == 'image/jpeg' or part.get_content_type() == 'image/png':
        attachment_name = part.get_filename()

        attachment_data = part.get_payload(decode=True)

        with open(attachment_name, 'wb') as file:
            file.write(attachment_data)

pop3_conn.quit()
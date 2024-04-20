import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Dane serwera SMTP
smtp_server = 'dsmka.wintertoad.xyz'
smtp_port = 587

sender = input("Podaj adres e-mail nadawcy: ")
password = input("Podaj hasło do konta e-mail: ")
recipient = input("Podaj adres e-mail odbiorcy: ")
smtp_username = input("Podaj nazwę użytkownika SMTP: ")
smtp_password = input("Podaj hasło SMTP: ")

message = MIMEMultipart('alternative')
message['Subject'] = 'Przykładowa wiadomość e-mail'
message['From'] = sender
message['To'] = recipient

html_content = '''
<html>
<body>
<p><b>TEST</b> <i>TEST</i> <u>TEST</u></p>
</body>
</html>
'''

html_part = MIMEText(html_content, 'html')
message.attach(html_part)

try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender, recipient, message.as_string())
    print('Wiadomość e-mail została wysłana.')
except Exception as e:
    print('Wystąpił błąd podczas wysyłania wiadomości:', str(e))
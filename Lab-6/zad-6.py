import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'dsmka.wintertoad.xyz'
smtp_port = 587

sender_email = input("Podaj adres e-mail nadawcy: ")
password = input("Podaj hasło do konta e-mail: ")
receiver_emails = input("Podaj adresy e-mail odbiorców (oddzielone przecinkami): ").split(',')
subject = input("Podaj temat wiadomości: ")
message = input("Podaj treść wiadomości: ")

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = ', '.join(receiver_emails)
msg['Subject'] = subject
msg.attach(MIMEText(message, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender_email, password)

    server.sendmail(sender_email, receiver_emails, msg.as_string())
    print("Wiadomość e-mail została wysłana pomyślnie!")

except Exception as e:
    print("Wystąpił błąd podczas wysyłania wiadomości e-mail:", str(e))

finally:
    server.quit()
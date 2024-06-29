import smtplib
import ssl

a = 10


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "emailsfromapp@gmail.com"
    password = "taca tplp imgh quss"
    receiver = "emailsfromapp@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

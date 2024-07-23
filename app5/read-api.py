import requests
import smtplib
import ssl


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


topic = "tesla"
url = "https://newsapi.org/v2/everything?q=tesla&sortBy=publishedAt&apiKey=1a568c9d2d434cdb8ba1789a6c0acd81&language=en"
request = requests.get(url)
content = request.json()
body = ""
for article in content["articles"][:20]:
    if article["title"] and article["description"] is not None:
        body = "Subject : Today's News" + "\n" + body + article["title"] + "\n" + article["description"] + "\n" + article["url"] + 2*"\n"

body = body.encode("utf-8")
send_email(body)

import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "lokeshb031@gmail.com"
password = "djutmbruwlqihdqh"

receiver = "lokeshb031@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Testing
HI!
How are you?"""

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)

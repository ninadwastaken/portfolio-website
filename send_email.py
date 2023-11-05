import smtplib, ssl, os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465


    username = 'ninad2eyes@gmail.com'
    password = os.getenv("portfolio_website_gmail_password")

    receiver = 'ninad2eyes@gmail.com'

    context = ssl.create_default_context()

    # with smtplib.SMTP("smtp.gmail.com") as server:
    #     server.starttls() and server.login(user=sender,
    #                                        password=password)
    #     server.sendmail(from_addr=sender,
    #                     to_addrs=receiver,
    #                     msg=message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

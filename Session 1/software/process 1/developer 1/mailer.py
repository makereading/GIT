import smtplib, ssl
import os

def send_mail(message, to_addr):
    port=465
    app_password=os.environ["GOOGLE_APP_PASSWORD"]
    context=ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as mysmtp:
        mysmtp.login("stark20236@gmail.com", app_password)
        mysmtp.sendmail("stark20236@gmail.com", to_addr ,message)


def to_mailinglist(message):
    to_addr = "kanchilug@freelists.org"
    message='''From: Iron Man <stark20236@gmail.com>
To: KanchiLUG mailing list <kanchilug@freelists.org>'''+message
    send_mail(message, to_addr)
    print("Mail sent to mailing list!")

def to_blog(message):
    to_addr = os.environ["WORDPRESS_EMAIL"] 
    message=f'''From: Iron Man <stark20236@gmail.com>
To: KanchiLUG Blog <{to_addr}>'''+message
    send_mail(message, to_addr)
    print("Post has been sent!")


from django.core.mail import send_mail
import environ
env = environ.Env()
environ.Env.read_env()

class Sendemail():

    def send_alert_email(book_title, book_isbn, book_author, emails):
        res = send_mail(
            'Intento de robo de libro',
            'Intentaron robar éste libro:\nTitle: {} - Author: {} - ISBN: {}'.format(book_title, book_author, book_isbn),
            env("EMAIL_HOST_USER"),
            emails,
            fail_silently=False
        )
        print(res)

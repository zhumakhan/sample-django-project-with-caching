from __future__ import absolute_import, unicode_literals


from celery.task import task


@task(name="email")
def send_async_email(emails, topic, message, html_message=None):
    from smtplib import SMTPException
    from django.core.mail import send_mail
    try:
        send_mail(topic,
                  message,
                  'someemail@mail.com',
                  emails, html_message=html_message,
                  fail_silently=False)
    except SMTPException as ex:
        print("ERROR IN EMAIL: ",ex)
    print('SENT TO ',emails)
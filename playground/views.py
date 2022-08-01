import contextlib
from django.core.mail import EmailMessage ,BadHeaderError,mail_admins
from django.http import HttpResponse
from templated_mail.mail import BaseEmailMessage
from django.shortcuts import render


def say_hello(request):
    # try:
    #     mail_admins('Subject', 'Body',html_message='<p>This is a test</p>')
    # except BadHeaderError:
    #     pass

    # try:
    #     message = EmailMessage('Subject', 'Body','mohamad@mvm.com' ,to=['ali.tt.com'])
    #     message.attach_file('playground/static/images/Capture.JPG')
    #     message.send()
    # except BadHeaderError:
    #     pass


    try:
        message = BaseEmailMessage(
            template_name='playground/emails/temp.html',
            context={'name': 'Mohamad'},
        )
        message.send(['ali.tt.com'])
    except BadHeaderError:
        pass

    return render(request, 'hello.html', {'name': 'Mosh'})

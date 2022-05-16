from flask_mail import Message
from flask import render_template
from . import mail

def mail_message(subject,template,to,**kwargs):
    sender_email = 'lorrainechepkemoi4@gmail.com'

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)
    
def thanks_message(subject,template,to,**kwargs):
    sender_email = 'lorrainechepkemoi4@gmail.com'

    email2 = Message(subject, sender=sender_email, recipients=[to])
    email2.body= render_template(template + ".txt",**kwargs)
    email2.html = render_template(template + ".html",**kwargs)
    mail.send(email2)
    
def notification_message(subject,template,to,**kwargs):
    sender_email = 'lorrainechepkemoi4@gmail.com'

    email2 = Message(subject, sender=sender_email, recipients=[to])
    email2.body= render_template(template + ".txt",**kwargs)
    email2.html = render_template(template + ".html",**kwargs)
    mail.send(email2)
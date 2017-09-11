# email framework

from flask_mail import Message
from app import app, mail
from flask import render_template
from config import ADMINS
from threading import Thread
from .decorators import async

# implement threading
@async
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)

# generic email
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject = subject, sender = sender, recipients = recipients)
    msg.body = text_body
    msg.html = html_body
    send_async_email(app, msg)

# email based on contact form
def contact_email(name, email, msg):
    send_email("[Website] %s contacted you." % name, email, ADMINS,
        render_template("contact_email.txt", name = name, msg = msg),
        render_template("contact_email.html", name = name, msg = msg)
    )

# email sent back to contacting user
def return_email(name, email):
    send_email("[J. Kelly Jr] Thank you for contacting me!", ADMINS[0], email.split(),
        render_template("return_email.txt", name = name),
        render_template("return_email.html", name = name)
    )

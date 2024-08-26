from flask_mail import Message
from web import mail

# function to send/handle message
def send_message(subject, sender, recipients, body):
    message = Message(subject=subject, sender=sender, recipients=recipients)
    message.body = body
    mail.send(message) #send email


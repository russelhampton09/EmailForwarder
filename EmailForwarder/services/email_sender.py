import smtplib, ssl
import yagmail
from config.config import Config
from services.iemail_sender import IEmailSender

class EmailSender(IEmailSender):
    def __init__(self, config: Config):
        self.sender = config.sender_email
        self.subject = "Automated message from Russel's Python App"
        self.message = config.sender_message
        self.sender = config.sender_email
        self.yag = yagmail.SMTP(config.sender_email, config.sender_key)
        

    def send(self, to):
        self.yag.send(to, self.subject, self.message)



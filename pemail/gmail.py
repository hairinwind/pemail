import smtplib
import sys
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.utils import COMMASPACE,formatdate
from email import encoders

def send_email_text(subject, text, 
    filename = [], 
    sender = 'yaoappemail@gmail.com',  receiver = ['yaoappemail@gmail.com'], 
    host = 'smtp.gmail.com', username = 'yaoappemail@gmail.com', password = ''):

    print('sending email...')
    assert type(receiver) == list

    if password == '':
        password = os.environ['GMAIL_PASSWORD']

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = COMMASPACE.join(receiver)
    msg['Subject'] = subject
    msg.attach(MIMEText(text))                 
 
    for file in filename:                      
        att = MIMEBase('application', 'octet-stream') 
        att.set_payload(open(file, 'rb').read())
        encoders.encode_base64(att)
        att.add_header('Content-Disposition', 'attachment; filename="%s"' % file)
        msg.attach(att)
 
    smtp = smtplib.SMTP(host)          
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(username,password)
    smtp.sendmail(sender,receiver, msg.as_string())
    smtp.close()


if __name__=="__main__":
    subject = "rbc funds"
    text = "test"
    send_email_text(subject,text)
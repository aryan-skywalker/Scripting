import smtplib
from email.message import EmailMessage
from string import Template
#Using html as template in python
from pathlib import Path
#instead of os to goto html path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Anakin Skywalker'
email['to'] = '2005716@kiit.ac.in'
email['subject'] = 'You got 52l annual job'

email.set_content(html.substitute({'name':'Aryan'}),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('rickbarbossa1982','HarryStyles#25')
    smtp.send_message(email)
    print('Email sent boss!')

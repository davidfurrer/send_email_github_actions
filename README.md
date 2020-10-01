# How to send emails with github actions and python


## Setting up gmail account for sending emails

To set up a Gmail address for testing your code, do the following:

1) [Create a new Google account.](https://accounts.google.com/signup)

2) Turn [Allow less secure apps to ON](https://myaccount.google.com/lesssecureapps). Be aware that this makes it easier for others to gain access to your account.



[reference](https://realpython.com/python-send-email/#option-1-setting-up-a-gmail-account-for-development)


## Github action file

This github action will send an email everyday at 5am UTC.

```
name: send email

on:
  schedule:
    - cron: "0 5 * * *"

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.7
      - name: Install dependencies and send email
        run: |
          python -m pip install --upgrade pip
          pip install pipenv 
          pipenv install
          pipenv run python src/send_email.py
```


## Plain text Email

```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender_email = "sender-gmail@gmail.com"
receiver_email = "receiver-email@gmail.com"
password = "password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header('Some Title', 'utf-8').encode()

body = 'Hello World!'

msg_content = MIMEText(body, 'plain', 'utf-8')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
```

## Html Email

```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender_email = "sender-gmail@gmail.com"
receiver_email = "receiver-email@gmail.com"
password = "password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header('Some Title', 'utf-8').encode()

html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
    </p>
  </body>
</html>
"""

msg_content = MIMEText(html, 'html')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
```

## With attachment

```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender_email = "your-sender-gmail@gmail.com"
receiver_email = "receiver-email@gmail.com"
password = "password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header('Daily Dose of Italian', 'utf-8').encode()

body = 'Hello World!'

msg_content = MIMEText(body, 'plain', 'utf-8')
msg.attach(msg_content)

with open('your_image.png', 'rb') as f:
    # set attachment mime and file name, the image type is png
    mime = MIMEBase('image', 'png', filename='img1.png')
    # add required header data:
    mime.add_header('Content-Disposition', 'attachment', filename='img1.png')
    mime.add_header('X-Attachment-Id', '0')
    mime.add_header('Content-ID', '<0>')
    # read attachment file content into the MIMEBase object
    mime.set_payload(f.read())
    # encode with base64
    encoders.encode_base64(mime)
    # add MIMEBase object to MIMEMultipart object
    msg.attach(mime)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
```


## With table from dataframe

```python
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import pandas as pd

df = pd.read_csv("file.csv")
html_table = df.to_html()

sender_email = "sender-gmail@gmail.com"
receiver_email = "receiver-email@gmail.com"
password = "password"

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = Header('Some Title', 'utf-8').encode()

html_message = f"""
<html>
  <head></head>
  <body>
    {html_table}
  </body>
</html>
"""

msg_content = MIMEText(html_message, 'html')
msg.attach(msg_content)

# Create secure connection with server and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
```


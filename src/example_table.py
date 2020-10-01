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

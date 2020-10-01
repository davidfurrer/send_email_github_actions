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

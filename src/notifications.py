import smtplib
from email.mime.text import MIMEText

def send_email_notification(to_email, subject, message):
    sender_email = "your_email@example.com"
    sender_password = "your_password"

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
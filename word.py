import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email():
    sender_email = "akromjonrustamov56@gmail.com"
    reciver_email = "akromjonrustamov56@gmail.com"
    password = "qhdcsnmozcnrngih"
    subject = "Subject of the email"
    body = "Body of the email"

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = reciver_email
    message['Subject'] = subject

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, password)
        text = message.as_string()
        server.sendmail(sender_email, reciver_email, text)


if __name__=="__main__":
    send_email()
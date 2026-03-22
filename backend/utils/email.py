from email.message import EmailMessage
from aiosmtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()


async def send_email_async(subject, recipient, body):
    message = EmailMessage()
    message["From"] = f"{os.getenv('MAIL_FROM')}"
    message["To"] = recipient
    message["Subject"] = subject
    message.set_content(body)

    smtp = SMTP(
        hostname=os.getenv("MAIL_HOST"),
        port=os.getenv("MAIL_PORT"),
        start_tls=True,
    )

    await smtp.connect()
    await smtp.starttls()
    await smtp.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
    await smtp.quit()

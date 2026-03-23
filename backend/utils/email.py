from fastapi_mail import ConnectionConfig
from aiosmtplib import SMTP
from dotenv import load_dotenv
import os

load_dotenv()

conf = ConnectionConfig(
    MAIL_USERNAME=os.getenv("MAIL_USERNAME"),
    MAIL_PASSWORD=os.getenv("MAIL_PASSWORD"),
    MAIL_FROM=os.getenv("MAIL_FROM"),
    MAIL_PORT=int(os.getenv("MAIL_PORT", "587")),
    MAIL_SERVER=os.getenv("MAIL_HOST"),
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)


async def send_email_async(subject, recipient, body):
    # message["From"] = f"{os.getenv('MAIL_FROM')}"
    # message["To"] = recipient
    # message["Subject"] = subject
    # message.set_content(body)

    smtp = SMTP(
        hostname=os.getenv("MAIL_HOST"),
        port=os.getenv("MAIL_PORT"),
        start_tls=True,
    )

    await smtp.connect()
    await smtp.starttls()
    await smtp.login(os.getenv("MAIL_USERNAME"), os.getenv("MAIL_PASSWORD"))
    await smtp.quit()

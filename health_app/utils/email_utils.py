from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
import os
from typing import List
from pydantic import EmailStr

conf = ConnectionConfig(
    MAIL_USERNAME="your_email@example.com",
    MAIL_PASSWORD="your_password",
    MAIL_FROM="your_email@example.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True
)

async def send_email_async(subject: str, email_to: List[EmailStr], body: str):
    """
    Sends an email asynchronously.
    """
    message = MessageSchema(
        subject=subject,
        recipients=email_to,
        body=body,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)


from email import message_from_string
from email.mime.multipart import MIMEMultipart
from typing import Any, Dict, Optional

from aiosmtplib import send
from pydantic import EmailStr

from app.core.config import settings


async def send_message(
    receiver: EmailStr,
    subject: str = "",
    html: str = "",
    environment: Optional[Dict[str, Any]] = None,
):
    message = MIMEMultipart("alternative")
    message["From"] = (settings.EMAIL_FROM_NAME, settings.EMAILS_FROM_EMAIL)
    message["To"] = receiver
    message["Subject"] = subject
    await send(
        message=message,
        host=settings.SMTP_HOST,
        port=settings.SMTP_PORT,
        use_tls=settings.SMTP_TLS,
        username=settings.SMTP_USER,
        password=settings.SMTP_PASSWORD,
    )

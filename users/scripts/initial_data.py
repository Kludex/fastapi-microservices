import asyncio
import logging
from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.users import User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def create_first_user(session: AsyncSession) -> None:
    email = settings.FIRST_USER_EMAIL
    password = get_password_hash(settings.FIRST_USER_PASSWORD.get_secret_value())
    result = await session.execute(select(User).where(User.email == email))
    user: Optional[User] = result.scalars().first()
    if user is None:
        session.add(User(email=email, hashed_password=password, is_superuser=True))
        await session.commit()


async def main():
    logger.info("Creating initial data")
    async with SessionLocal() as session:
        await create_first_user(session)
    logger.info("Initial data created")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

from typing import Optional

from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import is_valid_password
from app.models.users import User


async def get_user_by_id(session: AsyncSession, id: int) -> Optional[User]:
    result = await session.execute(select(User).where(User.id == id))
    return result.scalars().first()


async def get_user_by_email(session: AsyncSession, email: EmailStr) -> Optional[User]:
    result = await session.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def authenticate(
    session: AsyncSession, email: EmailStr, password: str
) -> Optional[User]:
    user = await get_user_by_email(session, email)
    if user is not None and is_valid_password(password, user.hashed_password):
        return user
    return None

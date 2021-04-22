from typing import List, Optional

from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash, is_valid_password
from app.models.users import User
from app.schemas.user import UserCreate


async def create(session: AsyncSession, user_in: UserCreate) -> User:
    hashed_password = get_password_hash(user_in.password)
    user = User(
        **user_in.dict(exclude={"password"}, exclude_none=True),
        hashed_password=hashed_password
    )
    session.add(user)
    await session.commit()
    return user


async def get_multi(
    session: AsyncSession, *, skip: int = 0, limit: int = 100
) -> List[User]:
    result = await session.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()


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

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.POSTGRES_URI, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session():
    async with SessionLocal() as session:
        yield session

from typing import Any, Dict

import humps
from sqlalchemy import inspect
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_async_engine(settings.POSTGRES_URI, echo=True)
SessionLocal = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return humps.depascalize(cls.__name__)

    def dict(self) -> Dict[str, Any]:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

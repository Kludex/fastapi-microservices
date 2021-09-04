from typing import Any, Dict

import humps
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return humps.depascalize(cls.__name__)

    def dict(self) -> Dict[str, Any]:
        return {c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs}

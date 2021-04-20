import asyncio

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from app.core.database import engine, get_session
from app.main import app


@pytest.fixture()
async def connection():
    async with engine.begin() as conn:
        yield conn
        await conn.rollback()


@pytest.fixture()
async def session(connection: AsyncConnection):
    async with AsyncSession(connection, expire_on_commit=False) as _session:
        yield _session


@pytest.fixture(autouse=True)
async def override_dependency(session: AsyncSession):
    app.dependency_overrides[get_session] = lambda: session


@pytest.fixture(scope="session", autouse=True)
def event_loop():
    """Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="function")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac, LifespanManager(app):
        yield ac

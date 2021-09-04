import asyncio
from typing import AsyncIterator, Dict, Iterator

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from users.api.deps import get_session
from users.core.config import settings
from users.core.database import engine
from users.main import app


@pytest.fixture()
async def connection() -> AsyncConnection:
    async with engine.begin() as conn:
        yield conn
        await conn.rollback()


@pytest.fixture()
async def session(connection: AsyncConnection) -> AsyncIterator[AsyncSession]:
    async with AsyncSession(connection, expire_on_commit=False) as _session:
        yield _session


@pytest.fixture(autouse=True)
async def override_dependency(session: AsyncSession) -> None:
    app.dependency_overrides[get_session] = lambda: session


@pytest.fixture(scope="session", autouse=True)
def event_loop() -> Iterator[asyncio.AbstractEventLoop]:
    """Reference: https://github.com/pytest-dev/pytest-asyncio/issues/38#issuecomment-264418154"""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture()
async def client() -> AsyncClient:
    async with AsyncClient(app=app, base_url="http://test") as ac, LifespanManager(app):
        yield ac


@pytest.fixture()
async def super_token_headers(client: AsyncClient) -> Dict[str, str]:
    login_data = {
        "username": settings().FIRST_USER_EMAIL,
        "password": settings().FIRST_USER_PASSWORD.get_secret_value(),
    }
    res = await client.post("/api/v1/login/", data=login_data)
    access_token = res.json()["access_token"]
    return {"Authorization": f"Bearer {access_token}"}

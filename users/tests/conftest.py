import asyncio
from typing import Dict

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from app.api.deps import get_session
from app.core.database import engine
from app.main import app
from tests.utils import (
    get_normal_token_headers,
    get_superuser_token_headers,
    initial_data,
)


@pytest.fixture(scope="session", autouse=True)
async def initial_resources():
    async with AsyncSession(engine, expire_on_commit=False) as session:
        await initial_data(session)


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


@pytest.fixture()
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac, LifespanManager(app):
        yield ac


@pytest.fixture()
async def superuser_token_headers(client: AsyncClient) -> Dict[str, str]:
    access_token = await get_superuser_token_headers(client)
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture()
async def normal_token_headers(client: AsyncClient) -> Dict[str, str]:
    access_token = await get_normal_token_headers(client)
    return {"Authorization": f"Bearer {access_token}"}

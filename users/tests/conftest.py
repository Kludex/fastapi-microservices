import asyncio
from typing import Dict, Optional

import pytest
from asgi_lifespan import LifespanManager
from httpx import AsyncClient
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncConnection, AsyncSession

from app.api.deps import get_session
from app.core.security import get_password_hash
from app.core.config import settings
from app.core.database import engine
from app.main import app
from app.models.users import User


@pytest.fixture(scope="session")
async def connection():
    async with engine.begin() as conn:
        yield conn
        await conn.rollback()


@pytest.fixture(scope="session")
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


@pytest.fixture(scope="session")
async def client():
    async with AsyncClient(app=app, base_url="http://test") as ac, LifespanManager(app):
        yield ac


@pytest.fixture()
async def superuser_token_headers(client: AsyncClient) -> Dict[str, str]:
    login_data = {
        "username": settings.FIRST_USER_EMAIL,
        "password": settings.FIRST_USER_PASSWORD.get_secret_value(),
    }
    res = await client.post("/api/v1/login/", data=login_data)
    access_token = res.json()["access_token"]
    return {"Authorization": f"Bearer {access_token}"}


@pytest.fixture(scope="session")
async def create_non_superuser(session: AsyncSession) -> Dict[str, str]:
    email = "test_user@test.com"
    password = "Ksd8nASD1_Hjns!P"
    hashed_password = get_password_hash(password)
    result = await session.execute(select(User).where(User.email == email))
    user: Optional[User] = result.scalars().first()
    if user is None:
        session.add(User(email=email, hashed_password=hashed_password, is_superuser=False))
        await session.commit()
    return {"email": email, "password": password}


@pytest.fixture(scope="session")
async def user_token_headers(client: AsyncClient, create_non_superuser: Dict[str, str]) -> Dict[str, str]:
    login_data = {
        "username": create_non_superuser["email"],
        "password": create_non_superuser["password"],
    }
    res = await client.post("/api/v1/login/", data=login_data)
    access_token = res.json()["access_token"]
    return {"Authorization": f"Bearer {access_token}"}

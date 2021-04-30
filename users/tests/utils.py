from typing import Dict

from httpx import AsyncClient
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash
from app.models.users import User

NORMAL_USER = {"username": "normal@test.com", "password": "normal"}
SUPER_USER = {"username": "super@test.com", "password": "super"}


async def initial_data(session: AsyncSession):
    users = [
        User(
            email=data["username"],
            hashed_password=get_password_hash(data["password"]),
        )
        for data in (NORMAL_USER, SUPER_USER)
    ]
    try:
        session.add_all(users)
        await session.commit()
    except IntegrityError:
        ...


async def get_token_headers(client: AsyncClient, data: Dict[str, str]):
    res = await client.post("/api/v1/login/", data=data)
    return res.json()["access_token"]


async def get_superuser_token_headers(client: AsyncClient):
    return await get_token_headers(client, SUPER_USER)


async def get_normal_token_headers(client: AsyncClient):
    return await get_token_headers(client, NORMAL_USER)

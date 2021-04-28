import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings


@pytest.mark.asyncio()
async def test_login(client: AsyncSession):
    login_data = {
        "username": settings.FIRST_USER_EMAIL,
        "password": settings.FIRST_USER_PASSWORD.get_secret_value(),
    }
    res = await client.post("/api/v1/login/", data=login_data)
    assert res.status_code == 200, res.json()
    assert res.json().get("token_type") == "bearer"
    assert "access_token" in res.json().keys()

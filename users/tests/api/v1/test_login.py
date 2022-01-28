import pytest
from sqlalchemy.ext.asyncio import AsyncSession

from tests.utils import NORMAL_USER


@pytest.mark.asyncio()
async def test_login(client: AsyncSession):
    res = await client.post("/api/v1/login/", data=NORMAL_USER)
    assert res.status_code == 200, res.json()
    assert res.json().get("token_type") == "bearer"
    assert "access_token" in res.json().keys()

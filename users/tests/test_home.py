import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_home(client: AsyncClient):
    res = await client.get("/api/v1/home")
    assert res.status_code == 200
    assert res.json() == "Hello World!"

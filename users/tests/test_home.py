from typing import Dict

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_home(client: AsyncClient, superuser_token_headers: Dict[str, str]):
    res = await client.get("/api/v1/home", headers=superuser_token_headers)
    assert res.status_code == 200
    assert res.json() == "Hello World!"

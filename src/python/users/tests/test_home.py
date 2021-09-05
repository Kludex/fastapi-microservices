from typing import Dict

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_home(client: AsyncClient, super_token_headers: Dict[str, str]) -> None:
    res = await client.get("/api/v1/home", headers=super_token_headers)
    assert res.status_code == 200
    assert res.json() == "Hello World!"

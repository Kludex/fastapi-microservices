from typing import Dict
from unittest.mock import Mock, patch

import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_post_task(client: AsyncClient, normal_token_headers: Dict[str, str]):
    job = Mock(job_id="job_id")
    with patch("app.core.redis.pool.enqueue_job", return_value=job):
        res = await client.post(
            "/api/v1/tasks", params={"message": "message"}, headers=normal_token_headers
        )
        assert res.status_code == 201, res.json()
        assert "id" in res.json()
        assert res.json()["id"] == "job_id"

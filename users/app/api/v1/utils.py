from fastapi import APIRouter, Depends

from app.api.deps import get_current_user
from app.core import redis
from app.models.users import User
from app.schemas.job import Job

router = APIRouter(prefix="/utils", tags=["Utils"])


@router.post("/test-arq/", response_model=Job, status_code=201)
async def test_arq(message: str, current_user: User = Depends(get_current_user)):
    """
    Test ARQ worker.
    """
    job = await redis.pool.enqueue_job("test_task", message)
    return {"id": job.job_id}

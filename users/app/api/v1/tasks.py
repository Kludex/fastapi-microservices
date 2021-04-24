from arq.jobs import Job as ArqJob
from fastapi import APIRouter

from app.core import redis
from app.schemas.job import Job

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post("/", response_model=Job, status_code=201)
async def create_task(message: str):
    job = await redis.pool.enqueue_job("test_task", message)
    return {"id": job.job_id}


@router.get("/{task_id}/")
async def get_task(task_id: str):
    job = ArqJob(task_id, redis.pool)
    return await job.info()

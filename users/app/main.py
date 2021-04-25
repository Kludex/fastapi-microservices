from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI

from app.api import router
from app.core import redis
from app.core.config import settings


async def create_redis_pool():
    redis.pool = await create_pool(
        RedisSettings(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
    )


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.add_event_handler("startup", create_redis_pool)
    return application


app = create_application()

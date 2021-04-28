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


async def close_redis_pool():
    redis.pool.close()


def create_application() -> FastAPI:
    application = FastAPI(title=settings.PROJECT_NAME)
    application.include_router(router)
    application.add_event_handler("startup", create_redis_pool)
    application.add_event_handler("shutdown", close_redis_pool)
    return application


app = create_application()

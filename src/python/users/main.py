from arq import create_pool
from arq.connections import RedisSettings
from fastapi import FastAPI

from users.api import router
from users.core import redis
from users.core.config import settings


async def create_redis_pool() -> None:
    redis.pool = await create_pool(
        RedisSettings(host=settings().REDIS_HOST, port=settings().REDIS_PORT)
    )


async def close_redis_pool() -> None:
    redis.pool.close()


def create_application() -> FastAPI:
    application = FastAPI(title=settings().PROJECT_NAME)
    application.include_router(router)
    application.add_event_handler("startup", create_redis_pool)
    application.add_event_handler("shutdown", close_redis_pool)
    return application


app = create_application()

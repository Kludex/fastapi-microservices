import asyncio

import uvloop
from arq.connections import RedisSettings

from worker.config import settings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def test_task(ctx: dict, word: str) -> str:
    await asyncio.sleep(10)
    return f"test task return {word}"


async def startup(ctx: dict) -> None:
    print("start")


async def shutdown(ctx: dict) -> None:
    print("end")


class WorkerSettings:
    functions = [test_task]
    redis_settings = RedisSettings(settings().REDIS_HOST, port=settings().REDIS_PORT)
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False

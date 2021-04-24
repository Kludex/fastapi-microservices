import asyncio
import os

import uvloop
from arq.connections import RedisSettings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

# NOTE(Marcelo): Do we want to have the same environment variables on worker and app?
REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
REDIS_PORT = os.getenv("REDIS_PORT", 6379)


async def test_task(ctx, word: str):
    await asyncio.sleep(10)
    return f"test task return {word}"


async def startup(ctx):
    print("start")


async def shutdown(ctx):
    print("end")


class WorkerSettings:
    functions = [test_task]
    redis_settings = RedisSettings(host=REDIS_HOST, port=REDIS_PORT)
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False

import asyncio
import logging

from tenacity import after_log, before_log, retry, stop_after_attempt, wait_fixed

from app.core.database import SessionLocal

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

max_tries = 60 * 5  # 5 minutes
wait_seconds = 1


@retry(
    stop=stop_after_attempt(max_tries),
    wait=wait_fixed(wait_seconds),
    before=before_log(logger, logging.INFO),
    after=after_log(logger, logging.WARN),
)
async def init() -> None:
    try:
        session = SessionLocal()
        # Try to create session to check if DB is awake
        await session.execute("SELECT 1")
    except Exception as exc:
        logger.error(exc)
        raise exc


async def main() -> None:
    logger.info("Initializing service")
    await init()
    logger.info("Service finished initializing")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

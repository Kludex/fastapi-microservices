from fastapi import FastAPI

from app.api import router
from app.core.database import Base, engine


async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


def create_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    application.add_event_handler("startup", startup)
    return application


app = create_application()

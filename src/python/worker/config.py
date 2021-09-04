from functools import cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379


@cache
def settings() -> Settings:
    return Settings()

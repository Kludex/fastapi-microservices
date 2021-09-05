import multiprocessing
from typing import Any, Callable, Dict, Protocol, Type

import uvicorn
from gunicorn.app.base import BaseApplication

from users.core.config import settings
from users.main import app


class ASGI3Protocol(Protocol):
    async def __call__(self, scope: dict, receive: Callable, send: Callable) -> None:
        ...


ASGI3Application = Type[ASGI3Protocol]


def number_of_workers() -> int:
    return (multiprocessing.cpu_count() * 2) + 1


class StandaloneApplication(BaseApplication):
    def __init__(self, application: ASGI3Application, options: Dict[str, Any] = None):
        self.options = options or {}
        self.application = application
        super().__init__()

    def load_config(self) -> None:
        config = {
            key: value
            for key, value in self.options.items()
            if key in self.cfg.settings and value is not None
        }
        for key, value in config.items():
            self.cfg.set(key.lower(), value)

    def load(self) -> ASGI3Application:
        return self.application


if __name__ == "__main__":
    if settings().ENV == "prod":
        options = {
            "bind": "%s:%s" % ("127.0.0.1", "8000"),
            "workers": number_of_workers(),
            "worker_class": "uvicorn.workers.UvicornWorker",
        }
        StandaloneApplication(app, options).run()
    else:
        uvicorn.run("main:app", reload=True)

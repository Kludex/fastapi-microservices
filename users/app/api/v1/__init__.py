from fastapi import APIRouter

from app.api.v1.home import router as home_router
from app.api.v1.login import router as login_router
from app.api.v1.tasks import router as tasks_router
from app.api.v1.users import router as users_router

router = APIRouter(prefix="/v1")
router.include_router(home_router)
router.include_router(login_router)
router.include_router(tasks_router)
router.include_router(users_router)

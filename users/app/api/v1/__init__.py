from fastapi import APIRouter

from app.api.v1.home import router as home_router

router = APIRouter(prefix="/v1")
router.include_router(home_router)

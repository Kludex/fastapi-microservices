from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["Home"])


@router.get("/")
async def home():
    return "Hello World!"

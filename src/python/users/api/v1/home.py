from fastapi import APIRouter, Depends

from users.api.deps import get_token_data

router = APIRouter(prefix="/home", tags=["Home"])


@router.get("/", dependencies=[Depends(get_token_data)])
async def home() -> str:
    return "Hello World!"


@router.get("/another/")
async def another() -> str:
    print("hi")
    return "Another Hello World!"

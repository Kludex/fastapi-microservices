from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_session, get_token_data

router = APIRouter(prefix="/home", tags=["Home"])


@router.get("/", dependencies=[Depends(get_token_data)])
async def home():
    return "Hello World!"


@router.get("/another/")
async def another(session: AsyncSession = Depends(get_session)):
    await session.execute("SELECT 1")

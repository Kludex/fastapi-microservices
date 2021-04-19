from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_session

router = APIRouter(prefix="/home", tags=["Home"])


@router.get("/")
async def home():
    return "Hello World!"


@router.get("/another")
async def another(session: AsyncSession = Depends(get_session)):
    await session.execute("SELECT 1")

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from users.api.deps import get_session
from users.core.security import authenticate, create_access_token
from users.schemas.token import Token

router = APIRouter(tags=["Login"])


@router.post("/login/", response_model=Token)
async def login(
    data: OAuth2PasswordRequestForm = Depends(),
    session: AsyncSession = Depends(get_session),
):
    user = await authenticate(session, email=data.username, password=data.password)
    if user is None:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    if not user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return {"access_token": create_access_token(user), "token_type": "bearer"}

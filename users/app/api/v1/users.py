from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import (
    get_current_superuser,
    get_current_user,
    get_session,
    on_superuser,
)
from app.crud import users as crud_user
from app.models.users import User
from app.schemas.user import UserCreate, UserOut

router = APIRouter(prefix="/users")


@router.get("/", response_model=List[UserOut], dependencies=[Depends(on_superuser)])
async def read_users(
    skip: int = 0, limit: int = 100, session: AsyncSession = Depends(get_session)
):
    """
    Retrieve users.
    """
    users = await crud_user.get_multi(session, skip=skip, limit=limit)
    return users


@router.post("/", response_model=UserOut, dependencies=[Depends(on_superuser)])
async def create_user(
    user_in: UserCreate, session: AsyncSession = Depends(get_session)
):
    """
    Create new user.
    """
    user = await crud_user.get_user_by_email(session, email=user_in.email)
    if user is not None:
        raise HTTPException(
            status_code=409,
            detail="The user with this username already exists in the system",
        )
    return await crud_user.create(session, user_in)


@router.get("/{user_id}/", response_model=UserOut)
async def read_user(
    user_id: int,
    current_user: User = Depends(get_current_user),
    session: AsyncSession = Depends(get_session),
):
    """
    Get a specific user by id.
    """
    user = await crud_user.get_user_by_id(session, id=user_id)
    if current_user.id == user_id:
        return current_user
    if not current_user.is_superuser:
        raise HTTPException(
            status_code=403, detail="The user doesn't have enough privileges"
        )
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete("/{user_id}/", status_code=204)
async def delete_user(
    user_id: int,
    current_user: User = Depends(get_current_superuser),
    session: AsyncSession = Depends(get_session),
):
    user = await crud_user.get_user_by_id(session, id=user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    if current_user.id == user.id:
        raise HTTPException(status_code=403, detail="User can't delete itself")
    await session.delete(user)
    await session.commit()

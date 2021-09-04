from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: bool = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserCreate(UserBase):
    email: EmailStr
    password: str


class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True


class UserInDB(UserBase):
    hashed_password: str


class UserUpdate(UserBase):
    password: Optional[str] = None


class UserUpdateDB(UserBase):
    hashed_password: str

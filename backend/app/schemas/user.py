from typing import Optional
from pydantic import BaseModel

from app.models.user import UserRole


class UserBase(BaseModel):
    name: str
    role: UserRole
    email: Optional[str] = None
    username: Optional[str] = None


class UserCreate(UserBase):
    password: Optional[str] = None


class UserRead(UserBase):
    user_id: int

    model_config = {"from_attributes": True}


class UserUpdate(BaseModel):
    name: Optional[str] = None
    role: Optional[UserRole] = None
    email: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None

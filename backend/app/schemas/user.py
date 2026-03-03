from typing import Optional
from pydantic import BaseModel

from app.models.user import UserRole


class UserBase(BaseModel):
    name: str
    role: UserRole
    email: Optional[str] = None


class UserCreate(UserBase):
    pass


class UserRead(UserBase):
    user_id: int

    model_config = {"from_attributes": True}

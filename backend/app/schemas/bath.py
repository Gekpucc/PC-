from typing import Optional

from pydantic import BaseModel


class BathBase(BaseModel):
    name: str
    type: Optional[str] = None
    chemical: Optional[str] = None
    current_status: Optional[str] = None


class BathCreate(BathBase):
    pass


class BathRead(BathBase):
    bath_id: int

    model_config = {"from_attributes": True}

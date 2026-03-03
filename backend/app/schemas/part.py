from typing import Optional
from pydantic import BaseModel


class PartBase(BaseModel):
    customer_id: int
    part_number: str
    description: Optional[str] = None
    material: Optional[str] = None
    spec: Optional[str] = None


class PartCreate(PartBase):
    pass


class PartRead(PartBase):
    part_id: int

    model_config = {"from_attributes": True}

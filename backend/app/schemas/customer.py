from typing import Optional
from pydantic import BaseModel


class CustomerBase(BaseModel):
    name: str
    contact: Optional[str] = None
    itar_flag: bool = False


class CustomerCreate(CustomerBase):
    pass


class CustomerRead(CustomerBase):
    customer_id: int

    model_config = {"from_attributes": True}

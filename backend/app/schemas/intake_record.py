from typing import Optional
from datetime import date
from pydantic import BaseModel


class IntakeRecordBase(BaseModel):
    po_id: int
    received_qty: int
    received_date: Optional[date] = None
    discrepancy_flag: bool = False
    tech_id: int


class IntakeRecordCreate(IntakeRecordBase):
    pass


class IntakeRecordRead(IntakeRecordBase):
    intake_id: int

    model_config = {"from_attributes": True}

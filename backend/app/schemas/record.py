from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class RecordBase(BaseModel):
    wo_id: int
    step_id: Optional[int] = None
    substep_id: Optional[int] = None
    bath_id: Optional[int] = None
    tech_id: Optional[int] = None
    timestamp: Optional[datetime] = None
    signoff: Optional[str] = None


class RecordCreate(RecordBase):
    pass


class RecordRead(RecordBase):
    record_id: int

    model_config = {"from_attributes": True}

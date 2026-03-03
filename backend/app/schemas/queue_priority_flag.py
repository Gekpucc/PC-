from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.models.queue_priority_flag import PriorityLevel


class QueuePriorityFlagBase(BaseModel):
    wo_id: int
    priority_level: PriorityLevel
    reason: Optional[str] = None
    set_by: int
    set_date: date


class QueuePriorityFlagCreate(QueuePriorityFlagBase):
    pass


class QueuePriorityFlagUpdate(BaseModel):
    priority_level: Optional[PriorityLevel] = None
    reason: Optional[str] = None
    set_by: Optional[int] = None
    set_date: Optional[date] = None


class QueuePriorityFlagRead(QueuePriorityFlagBase):
    priority_flag_id: int

    model_config = {"from_attributes": True}

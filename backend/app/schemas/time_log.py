from typing import Optional
from datetime import datetime

from pydantic import BaseModel, model_validator


class TimeLogBase(BaseModel):
    wo_id: int
    step_id: int
    tech_id: int
    clock_in: datetime
    clock_out: Optional[datetime] = None
    handoff_to: Optional[int] = None


class TimeLogCreate(TimeLogBase):
    pass


class TimeLogUpdate(BaseModel):
    clock_out: Optional[datetime] = None
    handoff_to: Optional[int] = None


class TimeLogRead(TimeLogBase):
    time_log_id: int
    duration: Optional[int] = None  # seconds; None when clock_out is not yet set

    model_config = {"from_attributes": True}

    @model_validator(mode="after")
    def compute_duration(self) -> "TimeLogRead":
        if self.clock_in is not None and self.clock_out is not None:
            self.duration = int((self.clock_out - self.clock_in).total_seconds())
        return self

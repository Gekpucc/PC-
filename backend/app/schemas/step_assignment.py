from typing import Optional
from datetime import datetime

from pydantic import BaseModel


class StepAssignmentBase(BaseModel):
    wo_id: int
    step_id: int
    tech_id: int
    claimed_at: datetime
    released_at: Optional[datetime] = None
    handoff_to: Optional[int] = None


class StepAssignmentCreate(StepAssignmentBase):
    pass


class StepAssignmentUpdate(BaseModel):
    released_at: Optional[datetime] = None
    handoff_to: Optional[int] = None


class StepAssignmentRead(StepAssignmentBase):
    assignment_id: int

    model_config = {"from_attributes": True}

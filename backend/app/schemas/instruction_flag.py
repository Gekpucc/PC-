from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.models.instruction_flag import FlagType, FlagStatus


class InstructionFlagBase(BaseModel):
    substep_id: int
    reported_by: int
    flag_type: FlagType
    description: Optional[str] = None
    status: FlagStatus = FlagStatus.open
    created_date: date


class InstructionFlagCreate(InstructionFlagBase):
    pass


class InstructionFlagUpdate(BaseModel):
    flag_type: Optional[FlagType] = None
    description: Optional[str] = None
    status: Optional[FlagStatus] = None


class InstructionFlagRead(InstructionFlagBase):
    flag_id: int

    model_config = {"from_attributes": True}

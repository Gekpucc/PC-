from typing import Optional

from pydantic import BaseModel


class StepFieldEntryBase(BaseModel):
    record_id: int
    step_field_id: int
    entered_value: Optional[str] = None


class StepFieldEntryCreate(StepFieldEntryBase):
    pass


class StepFieldEntryRead(StepFieldEntryBase):
    entry_id: int
    out_of_spec: bool

    model_config = {"from_attributes": True}

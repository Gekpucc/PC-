from typing import Optional

from pydantic import BaseModel


class StepBase(BaseModel):
    procedure_id: int
    section_id: Optional[int] = None
    sequence_order: float
    description: str
    spec_reference: Optional[str] = None
    requires_authorization: bool = False


class StepCreate(StepBase):
    pass


class StepRead(StepBase):
    step_id: int

    model_config = {"from_attributes": True}

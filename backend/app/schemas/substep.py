from typing import Optional

from pydantic import BaseModel


class SubStepBase(BaseModel):
    step_id: int
    instruction_text: str
    warning_flag: bool = False
    image_attachment: Optional[str] = None
    requires_signoff: bool = False


class SubStepCreate(SubStepBase):
    pass


class SubStepRead(SubStepBase):
    substep_id: int

    model_config = {"from_attributes": True}

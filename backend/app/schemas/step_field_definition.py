from typing import Any, Optional

from pydantic import BaseModel

from app.models.step_field_definition import FieldType


class StepFieldDefinitionBase(BaseModel):
    step_id: int
    field_type: FieldType
    field_label: str
    options: Optional[Any] = None
    required: bool = False
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    spec_limit_low: Optional[float] = None
    spec_limit_high: Optional[float] = None
    table_columns: Optional[Any] = None


class StepFieldDefinitionCreate(StepFieldDefinitionBase):
    pass


class StepFieldDefinitionRead(StepFieldDefinitionBase):
    step_field_id: int

    model_config = {"from_attributes": True}

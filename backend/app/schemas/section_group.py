from pydantic import BaseModel


class SectionGroupBase(BaseModel):
    work_plan_id: int
    name: str
    sequence_order: int


class SectionGroupCreate(SectionGroupBase):
    pass


class SectionGroupRead(SectionGroupBase):
    section_id: int

    model_config = {"from_attributes": True}

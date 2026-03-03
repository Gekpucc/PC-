from pydantic import BaseModel


class WorkPlanBase(BaseModel):
    name: str
    created_by: int


class WorkPlanCreate(WorkPlanBase):
    pass


class WorkPlanRead(WorkPlanBase):
    work_plan_id: int

    model_config = {"from_attributes": True}

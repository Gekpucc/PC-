from pydantic import BaseModel


class WorkPlanProcedureBase(BaseModel):
    work_plan_id: int
    procedure_id: int
    sequence_order: int


class WorkPlanProcedureCreate(WorkPlanProcedureBase):
    pass


class WorkPlanProcedureRead(WorkPlanProcedureBase):
    model_config = {"from_attributes": True}

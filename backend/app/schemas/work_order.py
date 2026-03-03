from typing import Optional
from datetime import date
from pydantic import BaseModel

from app.models.work_order import WOStatus, WOPriority


class WorkOrderBase(BaseModel):
    po_id: int
    part_id: int
    work_plan_id: Optional[int] = None
    status: WOStatus = WOStatus.received
    priority_level: WOPriority = WOPriority.normal
    created_date: Optional[date] = None
    due_date: Optional[date] = None


class WorkOrderCreate(WorkOrderBase):
    pass


class WorkOrderRead(WorkOrderBase):
    wo_id: int

    model_config = {"from_attributes": True}

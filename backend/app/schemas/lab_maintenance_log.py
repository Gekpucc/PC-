from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.models.lab_maintenance_log import TaskType


class LabMaintenanceLogBase(BaseModel):
    bath_id: Optional[int] = None
    tech_id: Optional[int] = None
    task_type: TaskType
    date_performed: Optional[date] = None
    result: Optional[str] = None
    next_due: Optional[date] = None


class LabMaintenanceLogCreate(LabMaintenanceLogBase):
    pass


class LabMaintenanceLogRead(LabMaintenanceLogBase):
    lab_maintenance_id: int

    model_config = {"from_attributes": True}

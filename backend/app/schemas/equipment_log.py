from typing import Optional
from datetime import date

from pydantic import BaseModel


class EquipmentLogBase(BaseModel):
    bath_id: int
    calibration_due: Optional[date] = None
    certification_expiry: Optional[date] = None
    maintenance_notes: Optional[str] = None
    status: Optional[str] = None


class EquipmentLogCreate(EquipmentLogBase):
    pass


class EquipmentLogRead(EquipmentLogBase):
    equipment_log_id: int

    model_config = {"from_attributes": True}

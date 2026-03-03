from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.models.coc import ExportFormat


class COCBase(BaseModel):
    wo_id: int
    generated_date: date
    approved_by: Optional[int] = None
    export_format: Optional[ExportFormat] = None
    attachment: Optional[str] = None


class COCCreate(COCBase):
    pass


class COCUpdate(BaseModel):
    approved_by: Optional[int] = None
    export_format: Optional[ExportFormat] = None
    attachment: Optional[str] = None


class COCRead(COCBase):
    coc_id: int

    model_config = {"from_attributes": True}

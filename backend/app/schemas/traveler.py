from typing import Optional
from datetime import date

from pydantic import BaseModel

from app.models.traveler import TravelerStatus


class TravelerBase(BaseModel):
    wo_id: int
    work_plan_id: int
    export_date: Optional[date] = None
    status: TravelerStatus = TravelerStatus.pending
    scanned_upload_attachment: Optional[str] = None


class TravelerCreate(TravelerBase):
    pass


class TravelerUpdate(BaseModel):
    export_date: Optional[date] = None
    status: Optional[TravelerStatus] = None
    scanned_upload_attachment: Optional[str] = None


class TravelerRead(TravelerBase):
    traveler_id: int

    model_config = {"from_attributes": True}

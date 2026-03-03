from typing import Optional

from pydantic import BaseModel

from app.models.nonconformance import NCRStatus


class NonconformanceBase(BaseModel):
    wo_id: int
    part_id: int
    opened_by: int
    disposition: Optional[str] = None
    status: NCRStatus = NCRStatus.open
    resolution_notes: Optional[str] = None


class NonconformanceCreate(NonconformanceBase):
    pass


class NonconformanceUpdate(BaseModel):
    disposition: Optional[str] = None
    status: Optional[NCRStatus] = None
    resolution_notes: Optional[str] = None


class NonconformanceRead(NonconformanceBase):
    ncr_id: int

    model_config = {"from_attributes": True}

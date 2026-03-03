from typing import Optional
from datetime import date

from pydantic import BaseModel


class WitnessRecordBase(BaseModel):
    wo_id: int
    inspector_name: str
    company: str
    date_witnessed: date
    signed_document_attachment: Optional[str] = None


class WitnessRecordCreate(WitnessRecordBase):
    pass


class WitnessRecordRead(WitnessRecordBase):
    witness_id: int

    model_config = {"from_attributes": True}

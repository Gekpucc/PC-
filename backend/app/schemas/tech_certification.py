from typing import Optional
from datetime import date

from pydantic import BaseModel


class TechCertificationBase(BaseModel):
    user_id: int
    procedure_id: int
    authorized_date: date
    expiry_date: Optional[date] = None
    authorized_by: int


class TechCertificationCreate(TechCertificationBase):
    pass


class TechCertificationRead(TechCertificationBase):
    cert_id: int

    model_config = {"from_attributes": True}

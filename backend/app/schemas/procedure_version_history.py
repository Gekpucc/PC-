from typing import Optional
from datetime import date

from pydantic import BaseModel


class ProcedureVersionHistoryBase(BaseModel):
    procedure_id: int
    version_number: str
    changed_by: int
    change_summary: Optional[str] = None
    archived_date: date
    previous_version_id: Optional[int] = None


class ProcedureVersionHistoryCreate(ProcedureVersionHistoryBase):
    pass


class ProcedureVersionHistoryRead(ProcedureVersionHistoryBase):
    version_id: int

    model_config = {"from_attributes": True}

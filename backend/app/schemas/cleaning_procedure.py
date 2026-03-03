from typing import Optional
from pydantic import BaseModel

from app.models.cleaning_procedure import ProcedureStatus


class CleaningProcedureBase(BaseModel):
    name: str
    version: str
    status: ProcedureStatus = ProcedureStatus.active
    document_number: Optional[str] = None
    spec_reference: Optional[str] = None


class CleaningProcedureCreate(CleaningProcedureBase):
    pass


class CleaningProcedureRead(CleaningProcedureBase):
    procedure_id: int

    model_config = {"from_attributes": True}

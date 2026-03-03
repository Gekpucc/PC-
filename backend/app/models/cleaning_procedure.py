import enum

from sqlalchemy import Column, Integer, String, Enum
from app.database import Base


class ProcedureStatus(str, enum.Enum):
    active = "active"
    retired = "retired"


class CleaningProcedure(Base):
    __tablename__ = "cleaning_procedures"

    procedure_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    status = Column(Enum(ProcedureStatus), nullable=False, default=ProcedureStatus.active)
    document_number = Column(String, nullable=True)
    spec_reference = Column(String, nullable=True)

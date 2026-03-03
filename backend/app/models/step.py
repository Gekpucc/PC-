from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey

from app.database import Base


class Step(Base):
    __tablename__ = "steps"

    step_id = Column(Integer, primary_key=True, index=True)
    procedure_id = Column(Integer, ForeignKey("cleaning_procedures.procedure_id"), nullable=False)
    section_id = Column(Integer, ForeignKey("section_groups.section_id"), nullable=True)
    sequence_order = Column(Float, nullable=False)
    description = Column(String, nullable=False)
    spec_reference = Column(String, nullable=True)
    requires_authorization = Column(Boolean, nullable=False, default=False)

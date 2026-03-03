from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.database import Base


class StepFieldEntry(Base):
    __tablename__ = "step_field_entries"

    entry_id = Column(Integer, primary_key=True, index=True)
    record_id = Column(Integer, ForeignKey("records.record_id"), nullable=False)
    step_field_id = Column(Integer, ForeignKey("step_field_definitions.step_field_id"), nullable=False)
    entered_value = Column(String, nullable=True)
    out_of_spec = Column(Boolean, nullable=False, default=False)

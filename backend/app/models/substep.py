from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

from app.database import Base


class SubStep(Base):
    __tablename__ = "substeps"

    substep_id = Column(Integer, primary_key=True, index=True)
    step_id = Column(Integer, ForeignKey("steps.step_id"), nullable=False)
    instruction_text = Column(String, nullable=False)
    warning_flag = Column(Boolean, nullable=False, default=False)
    image_attachment = Column(String, nullable=True)
    requires_signoff = Column(Boolean, nullable=False, default=False)

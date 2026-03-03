from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from app.database import Base


class Record(Base):
    __tablename__ = "records"

    record_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    step_id = Column(Integer, ForeignKey("steps.step_id"), nullable=True)
    substep_id = Column(Integer, ForeignKey("substeps.substep_id"), nullable=True)
    bath_id = Column(Integer, ForeignKey("baths.bath_id"), nullable=True)
    tech_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    timestamp = Column(DateTime, nullable=True)
    signoff = Column(String, nullable=True)

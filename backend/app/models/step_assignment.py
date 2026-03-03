from sqlalchemy import Column, Integer, DateTime, ForeignKey

from app.database import Base


class StepAssignment(Base):
    __tablename__ = "step_assignments"

    assignment_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    step_id = Column(Integer, ForeignKey("steps.step_id"), nullable=False)
    tech_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    claimed_at = Column(DateTime, nullable=False)
    released_at = Column(DateTime, nullable=True)
    handoff_to = Column(Integer, ForeignKey("users.user_id"), nullable=True)

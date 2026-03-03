from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class WorkPlan(Base):
    __tablename__ = "work_plans"

    work_plan_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)

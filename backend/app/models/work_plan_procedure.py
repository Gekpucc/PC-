from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base


class WorkPlanProcedure(Base):
    __tablename__ = "work_plan_procedures"

    work_plan_id = Column(Integer, ForeignKey("work_plans.work_plan_id"), primary_key=True)
    procedure_id = Column(Integer, ForeignKey("cleaning_procedures.procedure_id"), primary_key=True)
    sequence_order = Column(Integer, nullable=False)

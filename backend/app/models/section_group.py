from sqlalchemy import Column, Integer, String, ForeignKey

from app.database import Base


class SectionGroup(Base):
    __tablename__ = "section_groups"

    section_id = Column(Integer, primary_key=True, index=True)
    work_plan_id = Column(Integer, ForeignKey("work_plans.work_plan_id"), nullable=False)
    name = Column(String, nullable=False)
    sequence_order = Column(Integer, nullable=False)

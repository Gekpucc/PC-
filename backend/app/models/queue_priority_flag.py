import enum

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint

from app.database import Base


class PriorityLevel(str, enum.Enum):
    normal = "Normal"
    expedite = "Expedite"
    hold = "Hold"


class QueuePriorityFlag(Base):
    __tablename__ = "queue_priority_flags"
    __table_args__ = (UniqueConstraint("wo_id", name="uq_queue_priority_flag_wo"),)

    priority_flag_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    priority_level = Column(Enum(PriorityLevel), nullable=False, default=PriorityLevel.normal)
    reason = Column(String, nullable=True)
    set_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    set_date = Column(Date, nullable=False)

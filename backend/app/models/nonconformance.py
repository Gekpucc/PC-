import enum

from sqlalchemy import Column, Integer, String, Enum, ForeignKey

from app.database import Base


class NCRStatus(str, enum.Enum):
    open = "open"
    in_disposition = "in_disposition"
    closed = "closed"


class Nonconformance(Base):
    __tablename__ = "nonconformances"

    ncr_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    part_id = Column(Integer, ForeignKey("parts.part_id"), nullable=False)
    opened_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    disposition = Column(String, nullable=True)
    status = Column(Enum(NCRStatus), nullable=False, default=NCRStatus.open)
    resolution_notes = Column(String, nullable=True)

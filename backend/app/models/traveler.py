import enum

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey

from app.database import Base


class TravelerStatus(str, enum.Enum):
    pending = "pending"
    exported = "exported"
    scanned = "scanned"


class Traveler(Base):
    __tablename__ = "travelers"

    traveler_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    work_plan_id = Column(Integer, ForeignKey("work_plans.work_plan_id"), nullable=False)
    export_date = Column(Date, nullable=True)
    status = Column(Enum(TravelerStatus), nullable=False, default=TravelerStatus.pending)
    scanned_upload_attachment = Column(String, nullable=True)

import enum

from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey

from app.database import Base


class IssueStatus(str, enum.Enum):
    open = "open"
    in_progress = "in_progress"
    closed = "closed"


class IssueLog(Base):
    __tablename__ = "issue_logs"

    issue_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    reported_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    description = Column(String, nullable=False)
    status = Column(Enum(IssueStatus), nullable=False, default=IssueStatus.open)
    ncr_id = Column(Integer, ForeignKey("nonconformances.ncr_id"), nullable=True)
    customer_notified = Column(Boolean, nullable=False, default=False)
    customer_response = Column(String, nullable=True)
    resolution = Column(String, nullable=True)

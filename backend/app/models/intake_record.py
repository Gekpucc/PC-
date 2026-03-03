from sqlalchemy import Column, Integer, Boolean, Date, ForeignKey
from app.database import Base


class IntakeRecord(Base):
    __tablename__ = "intake_records"

    intake_id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.po_id"), nullable=False)
    received_qty = Column(Integer, nullable=False)
    received_date = Column(Date, nullable=True)
    discrepancy_flag = Column(Boolean, nullable=False, default=False)
    tech_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)

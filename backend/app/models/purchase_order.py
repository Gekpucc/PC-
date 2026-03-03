import enum

from sqlalchemy import Column, Integer, String, ForeignKey, Date, Numeric, Enum
from app.database import Base


class POStatus(str, enum.Enum):
    pending = "Pending"
    partially_received = "Partially Received"
    received = "Received"
    in_progress = "In Progress"
    on_hold = "On Hold"
    complete = "Complete"
    shipped = "Shipped"
    cancelled = "Cancelled"


class PurchaseOrder(Base):
    __tablename__ = "purchase_orders"

    po_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    part_number = Column(String, nullable=False)
    qty = Column(Integer, nullable=False)
    due_date = Column(Date, nullable=True)
    value = Column(Numeric(12, 2), nullable=True)
    status = Column(Enum(POStatus), nullable=False, default=POStatus.pending)

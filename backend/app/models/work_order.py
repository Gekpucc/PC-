import enum

from sqlalchemy import Column, Integer, ForeignKey, Date, Enum
from app.database import Base


class WOStatus(str, enum.Enum):
    received = "Received"
    intake_po_verification = "Intake / PO Verification"
    customer_outreach_hold = "Customer Outreach Hold"
    in_queue = "In Queue"
    pre_clean = "Pre-Clean"
    final_clean = "Final Clean"
    first_packaging = "1st Packaging"
    final_packaging = "Final Packaging"
    final_buyoff = "Final Buyoff"
    coc_generation = "COC Generation"
    shipped = "Shipped"
    ncr_hold = "NCR Hold"
    qa_rejection = "QA Rejection"


class WOPriority(str, enum.Enum):
    normal = "Normal"
    expedite = "Expedite"
    hold = "Hold"


class WorkOrder(Base):
    __tablename__ = "work_orders"

    wo_id = Column(Integer, primary_key=True, index=True)
    po_id = Column(Integer, ForeignKey("purchase_orders.po_id"), nullable=False)
    part_id = Column(Integer, ForeignKey("parts.part_id"), nullable=False)
    work_plan_id = Column(Integer, ForeignKey("work_plans.work_plan_id"), nullable=True)
    status = Column(Enum(WOStatus), nullable=False, default=WOStatus.received)
    priority_level = Column(Enum(WOPriority), nullable=False, default=WOPriority.normal)
    created_date = Column(Date, nullable=True)
    due_date = Column(Date, nullable=True)

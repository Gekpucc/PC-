from typing import Optional
from datetime import date
from decimal import Decimal
from pydantic import BaseModel

from app.models.purchase_order import POStatus


class PurchaseOrderBase(BaseModel):
    customer_id: int
    part_number: str
    qty: int
    due_date: Optional[date] = None
    value: Optional[Decimal] = None
    status: POStatus = POStatus.pending


class PurchaseOrderCreate(PurchaseOrderBase):
    pass


class PurchaseOrderRead(PurchaseOrderBase):
    po_id: int

    model_config = {"from_attributes": True}

from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.work_order import WorkOrder
from app.schemas.work_order import WorkOrderCreate, WorkOrderRead

router = APIRouter(prefix="/work-orders", tags=["Work Orders"])


@router.get("/", response_model=List[WorkOrderRead])
def list_work_orders(db: Session = Depends(get_db)):
    return db.query(WorkOrder).all()


@router.get("/{wo_id}", response_model=WorkOrderRead)
def get_work_order(wo_id: int, db: Session = Depends(get_db)):
    wo = db.query(WorkOrder).filter(WorkOrder.wo_id == wo_id).first()
    if not wo:
        raise HTTPException(status_code=404, detail="Work order not found")
    return wo


@router.post("/", response_model=WorkOrderRead, status_code=201)
def create_work_order(data: WorkOrderCreate, db: Session = Depends(get_db)):
    wo = WorkOrder(**data.model_dump())
    db.add(wo)
    db.commit()
    db.refresh(wo)
    return wo

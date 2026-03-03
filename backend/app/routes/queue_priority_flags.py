from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.queue_priority_flag import QueuePriorityFlag
from app.schemas.queue_priority_flag import (
    QueuePriorityFlagCreate,
    QueuePriorityFlagUpdate,
    QueuePriorityFlagRead,
)

router = APIRouter(prefix="/queue-priority-flags", tags=["Queue Priority Flags"])


@router.get("/", response_model=List[QueuePriorityFlagRead])
def list_queue_priority_flags(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(QueuePriorityFlag)
    if wo_id is not None:
        q = q.filter(QueuePriorityFlag.wo_id == wo_id)
    return q.all()


@router.get("/{priority_flag_id}", response_model=QueuePriorityFlagRead)
def get_queue_priority_flag(priority_flag_id: int, db: Session = Depends(get_db)):
    flag = db.query(QueuePriorityFlag).filter(
        QueuePriorityFlag.priority_flag_id == priority_flag_id
    ).first()
    if not flag:
        raise HTTPException(status_code=404, detail="Queue priority flag not found")
    return flag


@router.post("/", response_model=QueuePriorityFlagRead, status_code=201)
def create_queue_priority_flag(data: QueuePriorityFlagCreate, db: Session = Depends(get_db)):
    flag = QueuePriorityFlag(**data.model_dump())
    db.add(flag)
    db.commit()
    db.refresh(flag)
    return flag


@router.patch("/{priority_flag_id}", response_model=QueuePriorityFlagRead)
def update_queue_priority_flag(
    priority_flag_id: int, data: QueuePriorityFlagUpdate, db: Session = Depends(get_db)
):
    flag = db.query(QueuePriorityFlag).filter(
        QueuePriorityFlag.priority_flag_id == priority_flag_id
    ).first()
    if not flag:
        raise HTTPException(status_code=404, detail="Queue priority flag not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(flag, field, value)
    db.commit()
    db.refresh(flag)
    return flag

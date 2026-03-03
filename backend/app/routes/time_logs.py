from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.time_log import TimeLog
from app.schemas.time_log import TimeLogCreate, TimeLogUpdate, TimeLogRead

router = APIRouter(prefix="/time-logs", tags=["Time Logs"])


@router.get("/", response_model=List[TimeLogRead])
def list_time_logs(
    wo_id: Optional[int] = None,
    step_id: Optional[int] = None,
    tech_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(TimeLog)
    if wo_id is not None:
        q = q.filter(TimeLog.wo_id == wo_id)
    if step_id is not None:
        q = q.filter(TimeLog.step_id == step_id)
    if tech_id is not None:
        q = q.filter(TimeLog.tech_id == tech_id)
    return q.all()


@router.get("/{time_log_id}", response_model=TimeLogRead)
def get_time_log(time_log_id: int, db: Session = Depends(get_db)):
    log = db.query(TimeLog).filter(TimeLog.time_log_id == time_log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Time log not found")
    return log


@router.post("/", response_model=TimeLogRead, status_code=201)
def create_time_log(data: TimeLogCreate, db: Session = Depends(get_db)):
    log = TimeLog(**data.model_dump())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log


@router.patch("/{time_log_id}", response_model=TimeLogRead)
def update_time_log(time_log_id: int, data: TimeLogUpdate, db: Session = Depends(get_db)):
    log = db.query(TimeLog).filter(TimeLog.time_log_id == time_log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Time log not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(log, field, value)
    db.commit()
    db.refresh(log)
    return log

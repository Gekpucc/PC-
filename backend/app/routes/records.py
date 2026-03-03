from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.record import Record
from app.schemas.record import RecordCreate, RecordRead

router = APIRouter(prefix="/records", tags=["Records"])


@router.get("/", response_model=List[RecordRead])
def list_records(
    wo_id: Optional[int] = None,
    step_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Record)
    if wo_id is not None:
        q = q.filter(Record.wo_id == wo_id)
    if step_id is not None:
        q = q.filter(Record.step_id == step_id)
    return q.all()


@router.get("/{record_id}", response_model=RecordRead)
def get_record(record_id: int, db: Session = Depends(get_db)):
    record = db.query(Record).filter(Record.record_id == record_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Record not found")
    return record


@router.post("/", response_model=RecordRead, status_code=201)
def create_record(data: RecordCreate, db: Session = Depends(get_db)):
    record = Record(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

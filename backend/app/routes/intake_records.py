from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.intake_record import IntakeRecord
from app.schemas.intake_record import IntakeRecordCreate, IntakeRecordRead

router = APIRouter(prefix="/intake-records", tags=["Intake Records"])


@router.get("/", response_model=List[IntakeRecordRead])
def list_intake_records(db: Session = Depends(get_db)):
    return db.query(IntakeRecord).all()


@router.get("/{intake_id}", response_model=IntakeRecordRead)
def get_intake_record(intake_id: int, db: Session = Depends(get_db)):
    record = db.query(IntakeRecord).filter(IntakeRecord.intake_id == intake_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Intake record not found")
    return record


@router.post("/", response_model=IntakeRecordRead, status_code=201)
def create_intake_record(data: IntakeRecordCreate, db: Session = Depends(get_db)):
    record = IntakeRecord(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

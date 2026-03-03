from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.witness_record import WitnessRecord
from app.schemas.witness_record import WitnessRecordCreate, WitnessRecordRead

router = APIRouter(prefix="/witness-records", tags=["Witness Records"])


@router.get("/", response_model=List[WitnessRecordRead])
def list_witness_records(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(WitnessRecord)
    if wo_id is not None:
        q = q.filter(WitnessRecord.wo_id == wo_id)
    return q.all()


@router.get("/{witness_id}", response_model=WitnessRecordRead)
def get_witness_record(witness_id: int, db: Session = Depends(get_db)):
    record = db.query(WitnessRecord).filter(WitnessRecord.witness_id == witness_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Witness record not found")
    return record


@router.post("/", response_model=WitnessRecordRead, status_code=201)
def create_witness_record(data: WitnessRecordCreate, db: Session = Depends(get_db)):
    record = WitnessRecord(**data.model_dump())
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

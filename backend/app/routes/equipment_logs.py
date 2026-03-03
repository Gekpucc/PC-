from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.equipment_log import EquipmentLog
from app.schemas.equipment_log import EquipmentLogCreate, EquipmentLogRead

router = APIRouter(prefix="/equipment-logs", tags=["Equipment Logs"])


@router.get("/", response_model=List[EquipmentLogRead])
def list_equipment_logs(db: Session = Depends(get_db)):
    return db.query(EquipmentLog).all()


@router.get("/{equipment_log_id}", response_model=EquipmentLogRead)
def get_equipment_log(equipment_log_id: int, db: Session = Depends(get_db)):
    log = db.query(EquipmentLog).filter(EquipmentLog.equipment_log_id == equipment_log_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Equipment log not found")
    return log


@router.get("/bath/{bath_id}", response_model=EquipmentLogRead)
def get_equipment_log_by_bath(bath_id: int, db: Session = Depends(get_db)):
    log = db.query(EquipmentLog).filter(EquipmentLog.bath_id == bath_id).first()
    if not log:
        raise HTTPException(status_code=404, detail="Equipment log not found for this bath")
    return log


@router.post("/", response_model=EquipmentLogRead, status_code=201)
def create_equipment_log(data: EquipmentLogCreate, db: Session = Depends(get_db)):
    log = EquipmentLog(**data.model_dump())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

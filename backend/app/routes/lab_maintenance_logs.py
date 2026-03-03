from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.lab_maintenance_log import LabMaintenanceLog
from app.schemas.lab_maintenance_log import LabMaintenanceLogCreate, LabMaintenanceLogRead

router = APIRouter(prefix="/lab-maintenance-logs", tags=["Lab Maintenance Logs"])


@router.get("/", response_model=List[LabMaintenanceLogRead])
def list_lab_maintenance_logs(
    bath_id: Optional[int] = None,
    tech_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(LabMaintenanceLog)
    if bath_id is not None:
        q = q.filter(LabMaintenanceLog.bath_id == bath_id)
    if tech_id is not None:
        q = q.filter(LabMaintenanceLog.tech_id == tech_id)
    return q.all()


@router.get("/{lab_maintenance_id}", response_model=LabMaintenanceLogRead)
def get_lab_maintenance_log(lab_maintenance_id: int, db: Session = Depends(get_db)):
    log = db.query(LabMaintenanceLog).filter(
        LabMaintenanceLog.lab_maintenance_id == lab_maintenance_id
    ).first()
    if not log:
        raise HTTPException(status_code=404, detail="Lab maintenance log not found")
    return log


@router.post("/", response_model=LabMaintenanceLogRead, status_code=201)
def create_lab_maintenance_log(data: LabMaintenanceLogCreate, db: Session = Depends(get_db)):
    log = LabMaintenanceLog(**data.model_dump())
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

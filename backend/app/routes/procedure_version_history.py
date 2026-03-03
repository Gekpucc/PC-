from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.procedure_version_history import ProcedureVersionHistory
from app.schemas.procedure_version_history import (
    ProcedureVersionHistoryCreate,
    ProcedureVersionHistoryRead,
)

router = APIRouter(prefix="/procedure-version-history", tags=["Procedure Version History"])


@router.get("/", response_model=List[ProcedureVersionHistoryRead])
def list_procedure_version_history(
    procedure_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(ProcedureVersionHistory)
    if procedure_id is not None:
        q = q.filter(ProcedureVersionHistory.procedure_id == procedure_id)
    return q.all()


@router.get("/{version_id}", response_model=ProcedureVersionHistoryRead)
def get_procedure_version(version_id: int, db: Session = Depends(get_db)):
    version = db.query(ProcedureVersionHistory).filter(
        ProcedureVersionHistory.version_id == version_id
    ).first()
    if not version:
        raise HTTPException(status_code=404, detail="Procedure version not found")
    return version


@router.post("/", response_model=ProcedureVersionHistoryRead, status_code=201)
def create_procedure_version(data: ProcedureVersionHistoryCreate, db: Session = Depends(get_db)):
    version = ProcedureVersionHistory(**data.model_dump())
    db.add(version)
    db.commit()
    db.refresh(version)
    return version

from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.nonconformance import Nonconformance
from app.schemas.nonconformance import (
    NonconformanceCreate,
    NonconformanceUpdate,
    NonconformanceRead,
)

router = APIRouter(prefix="/nonconformances", tags=["Nonconformances"])


@router.get("/", response_model=List[NonconformanceRead])
def list_nonconformances(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Nonconformance)
    if wo_id is not None:
        q = q.filter(Nonconformance.wo_id == wo_id)
    return q.all()


@router.get("/{ncr_id}", response_model=NonconformanceRead)
def get_nonconformance(ncr_id: int, db: Session = Depends(get_db)):
    ncr = db.query(Nonconformance).filter(Nonconformance.ncr_id == ncr_id).first()
    if not ncr:
        raise HTTPException(status_code=404, detail="Nonconformance not found")
    return ncr


@router.post("/", response_model=NonconformanceRead, status_code=201)
def create_nonconformance(data: NonconformanceCreate, db: Session = Depends(get_db)):
    ncr = Nonconformance(**data.model_dump())
    db.add(ncr)
    db.commit()
    db.refresh(ncr)
    return ncr


@router.patch("/{ncr_id}", response_model=NonconformanceRead)
def update_nonconformance(
    ncr_id: int, data: NonconformanceUpdate, db: Session = Depends(get_db)
):
    ncr = db.query(Nonconformance).filter(Nonconformance.ncr_id == ncr_id).first()
    if not ncr:
        raise HTTPException(status_code=404, detail="Nonconformance not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(ncr, field, value)
    db.commit()
    db.refresh(ncr)
    return ncr

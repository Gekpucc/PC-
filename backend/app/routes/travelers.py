from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.traveler import Traveler
from app.schemas.traveler import TravelerCreate, TravelerUpdate, TravelerRead

router = APIRouter(prefix="/travelers", tags=["Travelers"])


@router.get("/", response_model=List[TravelerRead])
def list_travelers(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Traveler)
    if wo_id is not None:
        q = q.filter(Traveler.wo_id == wo_id)
    return q.all()


@router.get("/{traveler_id}", response_model=TravelerRead)
def get_traveler(traveler_id: int, db: Session = Depends(get_db)):
    traveler = db.query(Traveler).filter(Traveler.traveler_id == traveler_id).first()
    if not traveler:
        raise HTTPException(status_code=404, detail="Traveler not found")
    return traveler


@router.post("/", response_model=TravelerRead, status_code=201)
def create_traveler(data: TravelerCreate, db: Session = Depends(get_db)):
    traveler = Traveler(**data.model_dump())
    db.add(traveler)
    db.commit()
    db.refresh(traveler)
    return traveler


@router.patch("/{traveler_id}", response_model=TravelerRead)
def update_traveler(
    traveler_id: int, data: TravelerUpdate, db: Session = Depends(get_db)
):
    traveler = db.query(Traveler).filter(Traveler.traveler_id == traveler_id).first()
    if not traveler:
        raise HTTPException(status_code=404, detail="Traveler not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(traveler, field, value)
    db.commit()
    db.refresh(traveler)
    return traveler

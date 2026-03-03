from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.bath import Bath
from app.schemas.bath import BathCreate, BathRead

router = APIRouter(prefix="/baths", tags=["Baths"])


@router.get("/", response_model=List[BathRead])
def list_baths(db: Session = Depends(get_db)):
    return db.query(Bath).all()


@router.get("/{bath_id}", response_model=BathRead)
def get_bath(bath_id: int, db: Session = Depends(get_db)):
    bath = db.query(Bath).filter(Bath.bath_id == bath_id).first()
    if not bath:
        raise HTTPException(status_code=404, detail="Bath not found")
    return bath


@router.post("/", response_model=BathRead, status_code=201)
def create_bath(data: BathCreate, db: Session = Depends(get_db)):
    bath = Bath(**data.model_dump())
    db.add(bath)
    db.commit()
    db.refresh(bath)
    return bath

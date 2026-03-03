from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.cleaning_procedure import CleaningProcedure
from app.schemas.cleaning_procedure import CleaningProcedureCreate, CleaningProcedureRead

router = APIRouter(prefix="/cleaning-procedures", tags=["Cleaning Procedures"])


@router.get("/", response_model=List[CleaningProcedureRead])
def list_cleaning_procedures(db: Session = Depends(get_db)):
    return db.query(CleaningProcedure).all()


@router.get("/{procedure_id}", response_model=CleaningProcedureRead)
def get_cleaning_procedure(procedure_id: int, db: Session = Depends(get_db)):
    proc = db.query(CleaningProcedure).filter(CleaningProcedure.procedure_id == procedure_id).first()
    if not proc:
        raise HTTPException(status_code=404, detail="Cleaning procedure not found")
    return proc


@router.post("/", response_model=CleaningProcedureRead, status_code=201)
def create_cleaning_procedure(data: CleaningProcedureCreate, db: Session = Depends(get_db)):
    proc = CleaningProcedure(**data.model_dump())
    db.add(proc)
    db.commit()
    db.refresh(proc)
    return proc

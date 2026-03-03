from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.step import Step
from app.schemas.step import StepCreate, StepRead

router = APIRouter(prefix="/steps", tags=["Steps"])


@router.get("/", response_model=List[StepRead])
def list_steps(
    procedure_id: Optional[int] = None,
    section_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(Step)
    if procedure_id is not None:
        q = q.filter(Step.procedure_id == procedure_id)
    if section_id is not None:
        q = q.filter(Step.section_id == section_id)
    return q.order_by(Step.sequence_order).all()


@router.get("/{step_id}", response_model=StepRead)
def get_step(step_id: int, db: Session = Depends(get_db)):
    step = db.query(Step).filter(Step.step_id == step_id).first()
    if not step:
        raise HTTPException(status_code=404, detail="Step not found")
    return step


@router.post("/", response_model=StepRead, status_code=201)
def create_step(data: StepCreate, db: Session = Depends(get_db)):
    step = Step(**data.model_dump())
    db.add(step)
    db.commit()
    db.refresh(step)
    return step

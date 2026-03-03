from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.substep import SubStep
from app.schemas.substep import SubStepCreate, SubStepRead

router = APIRouter(prefix="/substeps", tags=["Sub-Steps"])


@router.get("/", response_model=List[SubStepRead])
def list_substeps(step_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(SubStep)
    if step_id is not None:
        q = q.filter(SubStep.step_id == step_id)
    return q.all()


@router.get("/{substep_id}", response_model=SubStepRead)
def get_substep(substep_id: int, db: Session = Depends(get_db)):
    substep = db.query(SubStep).filter(SubStep.substep_id == substep_id).first()
    if not substep:
        raise HTTPException(status_code=404, detail="Sub-step not found")
    return substep


@router.post("/", response_model=SubStepRead, status_code=201)
def create_substep(data: SubStepCreate, db: Session = Depends(get_db)):
    substep = SubStep(**data.model_dump())
    db.add(substep)
    db.commit()
    db.refresh(substep)
    return substep

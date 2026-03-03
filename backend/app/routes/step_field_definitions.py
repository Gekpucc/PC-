from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.step_field_definition import StepFieldDefinition
from app.schemas.step_field_definition import StepFieldDefinitionCreate, StepFieldDefinitionRead

router = APIRouter(prefix="/step-field-definitions", tags=["Step Field Definitions"])


@router.get("/", response_model=List[StepFieldDefinitionRead])
def list_step_field_definitions(step_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(StepFieldDefinition)
    if step_id is not None:
        q = q.filter(StepFieldDefinition.step_id == step_id)
    return q.all()


@router.get("/{step_field_id}", response_model=StepFieldDefinitionRead)
def get_step_field_definition(step_field_id: int, db: Session = Depends(get_db)):
    sfd = db.query(StepFieldDefinition).filter(StepFieldDefinition.step_field_id == step_field_id).first()
    if not sfd:
        raise HTTPException(status_code=404, detail="Step field definition not found")
    return sfd


@router.post("/", response_model=StepFieldDefinitionRead, status_code=201)
def create_step_field_definition(data: StepFieldDefinitionCreate, db: Session = Depends(get_db)):
    sfd = StepFieldDefinition(**data.model_dump())
    db.add(sfd)
    db.commit()
    db.refresh(sfd)
    return sfd

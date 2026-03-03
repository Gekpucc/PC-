from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.step_assignment import StepAssignment
from app.schemas.step_assignment import StepAssignmentCreate, StepAssignmentUpdate, StepAssignmentRead

router = APIRouter(prefix="/step-assignments", tags=["Step Assignments"])


@router.get("/", response_model=List[StepAssignmentRead])
def list_step_assignments(
    wo_id: Optional[int] = None,
    step_id: Optional[int] = None,
    tech_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(StepAssignment)
    if wo_id is not None:
        q = q.filter(StepAssignment.wo_id == wo_id)
    if step_id is not None:
        q = q.filter(StepAssignment.step_id == step_id)
    if tech_id is not None:
        q = q.filter(StepAssignment.tech_id == tech_id)
    return q.all()


@router.get("/{assignment_id}", response_model=StepAssignmentRead)
def get_step_assignment(assignment_id: int, db: Session = Depends(get_db)):
    assignment = db.query(StepAssignment).filter(
        StepAssignment.assignment_id == assignment_id
    ).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Step assignment not found")
    return assignment


@router.post("/", response_model=StepAssignmentRead, status_code=201)
def create_step_assignment(data: StepAssignmentCreate, db: Session = Depends(get_db)):
    assignment = StepAssignment(**data.model_dump())
    db.add(assignment)
    db.commit()
    db.refresh(assignment)
    return assignment


@router.patch("/{assignment_id}", response_model=StepAssignmentRead)
def update_step_assignment(
    assignment_id: int, data: StepAssignmentUpdate, db: Session = Depends(get_db)
):
    assignment = db.query(StepAssignment).filter(
        StepAssignment.assignment_id == assignment_id
    ).first()
    if not assignment:
        raise HTTPException(status_code=404, detail="Step assignment not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(assignment, field, value)
    db.commit()
    db.refresh(assignment)
    return assignment

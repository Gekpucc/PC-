from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.step_field_definition import StepFieldDefinition
from app.models.step_field_entry import StepFieldEntry
from app.schemas.step_field_entry import StepFieldEntryCreate, StepFieldEntryRead

router = APIRouter(prefix="/step-field-entries", tags=["Step Field Entries"])


def _compute_out_of_spec(entered_value: Optional[str], sfd: StepFieldDefinition) -> bool:
    if sfd.spec_limit_low is None and sfd.spec_limit_high is None:
        return False
    if entered_value is None:
        return False
    try:
        val = float(entered_value)
    except ValueError:
        return False
    if sfd.spec_limit_low is not None and val < sfd.spec_limit_low:
        return True
    if sfd.spec_limit_high is not None and val > sfd.spec_limit_high:
        return True
    return False


@router.get("/", response_model=List[StepFieldEntryRead])
def list_step_field_entries(
    record_id: Optional[int] = None,
    step_field_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(StepFieldEntry)
    if record_id is not None:
        q = q.filter(StepFieldEntry.record_id == record_id)
    if step_field_id is not None:
        q = q.filter(StepFieldEntry.step_field_id == step_field_id)
    return q.all()


@router.get("/{entry_id}", response_model=StepFieldEntryRead)
def get_step_field_entry(entry_id: int, db: Session = Depends(get_db)):
    entry = db.query(StepFieldEntry).filter(StepFieldEntry.entry_id == entry_id).first()
    if not entry:
        raise HTTPException(status_code=404, detail="Step field entry not found")
    return entry


@router.post("/", response_model=StepFieldEntryRead, status_code=201)
def create_step_field_entry(data: StepFieldEntryCreate, db: Session = Depends(get_db)):
    sfd = db.query(StepFieldDefinition).filter(
        StepFieldDefinition.step_field_id == data.step_field_id
    ).first()
    if not sfd:
        raise HTTPException(status_code=404, detail="Step field definition not found")
    out_of_spec = _compute_out_of_spec(data.entered_value, sfd)
    entry = StepFieldEntry(**data.model_dump(), out_of_spec=out_of_spec)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

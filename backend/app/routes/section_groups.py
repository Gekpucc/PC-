from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.section_group import SectionGroup
from app.schemas.section_group import SectionGroupCreate, SectionGroupRead

router = APIRouter(prefix="/section-groups", tags=["Section Groups"])


@router.get("/", response_model=List[SectionGroupRead])
def list_section_groups(work_plan_id: Optional[int] = None, db: Session = Depends(get_db)):
    q = db.query(SectionGroup)
    if work_plan_id is not None:
        q = q.filter(SectionGroup.work_plan_id == work_plan_id)
    return q.order_by(SectionGroup.sequence_order).all()


@router.get("/{section_id}", response_model=SectionGroupRead)
def get_section_group(section_id: int, db: Session = Depends(get_db)):
    sg = db.query(SectionGroup).filter(SectionGroup.section_id == section_id).first()
    if not sg:
        raise HTTPException(status_code=404, detail="Section group not found")
    return sg


@router.post("/", response_model=SectionGroupRead, status_code=201)
def create_section_group(data: SectionGroupCreate, db: Session = Depends(get_db)):
    sg = SectionGroup(**data.model_dump())
    db.add(sg)
    db.commit()
    db.refresh(sg)
    return sg

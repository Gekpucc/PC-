from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tag_template import TagTemplate
from app.schemas.tag_template import TagTemplateCreate, TagTemplateUpdate, TagTemplateRead

router = APIRouter(prefix="/tag-templates", tags=["Tag Templates"])


@router.get("/", response_model=List[TagTemplateRead])
def list_tag_templates(
    part_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(TagTemplate)
    if part_id is not None:
        q = q.filter(TagTemplate.part_id == part_id)
    return q.all()


@router.get("/{tag_template_id}", response_model=TagTemplateRead)
def get_tag_template(tag_template_id: int, db: Session = Depends(get_db)):
    template = db.query(TagTemplate).filter(TagTemplate.tag_template_id == tag_template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Tag template not found")
    return template


@router.post("/", response_model=TagTemplateRead, status_code=201)
def create_tag_template(data: TagTemplateCreate, db: Session = Depends(get_db)):
    template = TagTemplate(**data.model_dump())
    db.add(template)
    db.commit()
    db.refresh(template)
    return template


@router.patch("/{tag_template_id}", response_model=TagTemplateRead)
def update_tag_template(
    tag_template_id: int, data: TagTemplateUpdate, db: Session = Depends(get_db)
):
    template = db.query(TagTemplate).filter(TagTemplate.tag_template_id == tag_template_id).first()
    if not template:
        raise HTTPException(status_code=404, detail="Tag template not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(template, field, value)
    db.commit()
    db.refresh(template)
    return template

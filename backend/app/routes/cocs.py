from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.coc import COC
from app.schemas.coc import COCCreate, COCUpdate, COCRead

router = APIRouter(prefix="/cocs", tags=["COCs"])


@router.get("/", response_model=List[COCRead])
def list_cocs(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(COC)
    if wo_id is not None:
        q = q.filter(COC.wo_id == wo_id)
    return q.all()


@router.get("/{coc_id}", response_model=COCRead)
def get_coc(coc_id: int, db: Session = Depends(get_db)):
    coc = db.query(COC).filter(COC.coc_id == coc_id).first()
    if not coc:
        raise HTTPException(status_code=404, detail="COC not found")
    return coc


@router.post("/", response_model=COCRead, status_code=201)
def create_coc(data: COCCreate, db: Session = Depends(get_db)):
    coc = COC(**data.model_dump())
    db.add(coc)
    db.commit()
    db.refresh(coc)
    return coc


@router.patch("/{coc_id}", response_model=COCRead)
def update_coc(coc_id: int, data: COCUpdate, db: Session = Depends(get_db)):
    coc = db.query(COC).filter(COC.coc_id == coc_id).first()
    if not coc:
        raise HTTPException(status_code=404, detail="COC not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(coc, field, value)
    db.commit()
    db.refresh(coc)
    return coc

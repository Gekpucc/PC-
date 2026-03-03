from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.instruction_flag import InstructionFlag
from app.schemas.instruction_flag import (
    InstructionFlagCreate,
    InstructionFlagUpdate,
    InstructionFlagRead,
)

router = APIRouter(prefix="/instruction-flags", tags=["Instruction Flags"])


@router.get("/", response_model=List[InstructionFlagRead])
def list_instruction_flags(
    substep_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(InstructionFlag)
    if substep_id is not None:
        q = q.filter(InstructionFlag.substep_id == substep_id)
    return q.all()


@router.get("/{flag_id}", response_model=InstructionFlagRead)
def get_instruction_flag(flag_id: int, db: Session = Depends(get_db)):
    flag = db.query(InstructionFlag).filter(InstructionFlag.flag_id == flag_id).first()
    if not flag:
        raise HTTPException(status_code=404, detail="Instruction flag not found")
    return flag


@router.post("/", response_model=InstructionFlagRead, status_code=201)
def create_instruction_flag(data: InstructionFlagCreate, db: Session = Depends(get_db)):
    flag = InstructionFlag(**data.model_dump())
    db.add(flag)
    db.commit()
    db.refresh(flag)
    return flag


@router.patch("/{flag_id}", response_model=InstructionFlagRead)
def update_instruction_flag(
    flag_id: int, data: InstructionFlagUpdate, db: Session = Depends(get_db)
):
    flag = db.query(InstructionFlag).filter(InstructionFlag.flag_id == flag_id).first()
    if not flag:
        raise HTTPException(status_code=404, detail="Instruction flag not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(flag, field, value)
    db.commit()
    db.refresh(flag)
    return flag

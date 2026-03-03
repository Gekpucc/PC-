from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.work_plan import WorkPlan
from app.models.work_plan_procedure import WorkPlanProcedure
from app.schemas.work_plan import WorkPlanCreate, WorkPlanRead
from app.schemas.work_plan_procedure import WorkPlanProcedureCreate, WorkPlanProcedureRead

router = APIRouter(prefix="/work-plans", tags=["Work Plans"])


@router.get("/", response_model=List[WorkPlanRead])
def list_work_plans(db: Session = Depends(get_db)):
    return db.query(WorkPlan).all()


@router.get("/{work_plan_id}", response_model=WorkPlanRead)
def get_work_plan(work_plan_id: int, db: Session = Depends(get_db)):
    plan = db.query(WorkPlan).filter(WorkPlan.work_plan_id == work_plan_id).first()
    if not plan:
        raise HTTPException(status_code=404, detail="Work plan not found")
    return plan


@router.post("/", response_model=WorkPlanRead, status_code=201)
def create_work_plan(data: WorkPlanCreate, db: Session = Depends(get_db)):
    plan = WorkPlan(**data.model_dump())
    db.add(plan)
    db.commit()
    db.refresh(plan)
    return plan


@router.get("/{work_plan_id}/procedures", response_model=List[WorkPlanProcedureRead])
def list_work_plan_procedures(work_plan_id: int, db: Session = Depends(get_db)):
    return db.query(WorkPlanProcedure).filter(WorkPlanProcedure.work_plan_id == work_plan_id).all()


@router.post("/{work_plan_id}/procedures", response_model=WorkPlanProcedureRead, status_code=201)
def add_procedure_to_work_plan(
    work_plan_id: int,
    data: WorkPlanProcedureCreate,
    db: Session = Depends(get_db),
):
    if data.work_plan_id != work_plan_id:
        raise HTTPException(status_code=400, detail="work_plan_id in body must match URL")
    entry = WorkPlanProcedure(**data.model_dump())
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry

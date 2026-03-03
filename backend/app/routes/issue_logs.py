from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.issue_log import IssueLog
from app.schemas.issue_log import IssueLogCreate, IssueLogUpdate, IssueLogRead

router = APIRouter(prefix="/issue-logs", tags=["Issue Logs"])


@router.get("/", response_model=List[IssueLogRead])
def list_issue_logs(
    wo_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(IssueLog)
    if wo_id is not None:
        q = q.filter(IssueLog.wo_id == wo_id)
    return q.all()


@router.get("/{issue_id}", response_model=IssueLogRead)
def get_issue_log(issue_id: int, db: Session = Depends(get_db)):
    issue = db.query(IssueLog).filter(IssueLog.issue_id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue log not found")
    return issue


@router.post("/", response_model=IssueLogRead, status_code=201)
def create_issue_log(data: IssueLogCreate, db: Session = Depends(get_db)):
    issue = IssueLog(**data.model_dump())
    db.add(issue)
    db.commit()
    db.refresh(issue)
    return issue


@router.patch("/{issue_id}", response_model=IssueLogRead)
def update_issue_log(
    issue_id: int, data: IssueLogUpdate, db: Session = Depends(get_db)
):
    issue = db.query(IssueLog).filter(IssueLog.issue_id == issue_id).first()
    if not issue:
        raise HTTPException(status_code=404, detail="Issue log not found")
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(issue, field, value)
    db.commit()
    db.refresh(issue)
    return issue

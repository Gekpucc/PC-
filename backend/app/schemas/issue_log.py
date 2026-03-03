from typing import Optional

from pydantic import BaseModel

from app.models.issue_log import IssueStatus


class IssueLogBase(BaseModel):
    wo_id: int
    reported_by: int
    description: str
    status: IssueStatus = IssueStatus.open
    ncr_id: Optional[int] = None
    customer_notified: bool = False
    customer_response: Optional[str] = None
    resolution: Optional[str] = None


class IssueLogCreate(IssueLogBase):
    pass


class IssueLogUpdate(BaseModel):
    description: Optional[str] = None
    status: Optional[IssueStatus] = None
    ncr_id: Optional[int] = None
    customer_notified: Optional[bool] = None
    customer_response: Optional[str] = None
    resolution: Optional[str] = None


class IssueLogRead(IssueLogBase):
    issue_id: int

    model_config = {"from_attributes": True}

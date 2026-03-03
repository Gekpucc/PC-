from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.tech_certification import TechCertification
from app.schemas.tech_certification import TechCertificationCreate, TechCertificationRead

router = APIRouter(prefix="/tech-certifications", tags=["Tech Certifications"])


@router.get("/", response_model=List[TechCertificationRead])
def list_tech_certifications(
    user_id: Optional[int] = None,
    procedure_id: Optional[int] = None,
    db: Session = Depends(get_db),
):
    q = db.query(TechCertification)
    if user_id is not None:
        q = q.filter(TechCertification.user_id == user_id)
    if procedure_id is not None:
        q = q.filter(TechCertification.procedure_id == procedure_id)
    return q.all()


@router.get("/{cert_id}", response_model=TechCertificationRead)
def get_tech_certification(cert_id: int, db: Session = Depends(get_db)):
    cert = db.query(TechCertification).filter(TechCertification.cert_id == cert_id).first()
    if not cert:
        raise HTTPException(status_code=404, detail="Tech certification not found")
    return cert


@router.post("/", response_model=TechCertificationRead, status_code=201)
def create_tech_certification(data: TechCertificationCreate, db: Session = Depends(get_db)):
    cert = TechCertification(**data.model_dump())
    db.add(cert)
    db.commit()
    db.refresh(cert)
    return cert

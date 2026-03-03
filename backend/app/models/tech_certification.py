from sqlalchemy import Column, Integer, Date, ForeignKey

from app.database import Base


class TechCertification(Base):
    __tablename__ = "tech_certifications"

    cert_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    procedure_id = Column(Integer, ForeignKey("cleaning_procedures.procedure_id"), nullable=False)
    authorized_date = Column(Date, nullable=False)
    expiry_date = Column(Date, nullable=True)
    authorized_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)

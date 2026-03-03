from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.database import Base


class WitnessRecord(Base):
    __tablename__ = "witness_records"

    witness_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    inspector_name = Column(String, nullable=False)
    company = Column(String, nullable=False)
    date_witnessed = Column(Date, nullable=False)
    signed_document_attachment = Column(String, nullable=True)

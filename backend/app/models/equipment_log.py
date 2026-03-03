from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.database import Base


class EquipmentLog(Base):
    __tablename__ = "equipment_logs"

    equipment_log_id = Column(Integer, primary_key=True, index=True)
    bath_id = Column(Integer, ForeignKey("baths.bath_id"), nullable=False, unique=True)
    calibration_due = Column(Date, nullable=True)
    certification_expiry = Column(Date, nullable=True)
    maintenance_notes = Column(String, nullable=True)
    status = Column(String, nullable=True)

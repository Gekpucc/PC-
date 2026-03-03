import enum

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey

from app.database import Base


class TaskType(str, enum.Enum):
    titration = "titration"
    filter = "filter"
    sealer_check = "sealer_check"


class LabMaintenanceLog(Base):
    __tablename__ = "lab_maintenance_logs"

    lab_maintenance_id = Column(Integer, primary_key=True, index=True)
    bath_id = Column(Integer, ForeignKey("baths.bath_id"), nullable=True)
    tech_id = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    task_type = Column(Enum(TaskType), nullable=False)
    date_performed = Column(Date, nullable=True)
    result = Column(String, nullable=True)
    next_due = Column(Date, nullable=True)

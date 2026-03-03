import enum

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey, UniqueConstraint

from app.database import Base


class ExportFormat(str, enum.Enum):
    pdf = "pdf"
    word = "word"


class COC(Base):
    __tablename__ = "cocs"
    __table_args__ = (UniqueConstraint("wo_id", name="uq_coc_wo"),)

    coc_id = Column(Integer, primary_key=True, index=True)
    wo_id = Column(Integer, ForeignKey("work_orders.wo_id"), nullable=False)
    generated_date = Column(Date, nullable=False)
    approved_by = Column(Integer, ForeignKey("users.user_id"), nullable=True)
    export_format = Column(Enum(ExportFormat), nullable=True)
    attachment = Column(String, nullable=True)

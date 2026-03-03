from sqlalchemy import Column, Integer, String, Date, ForeignKey

from app.database import Base


class ProcedureVersionHistory(Base):
    __tablename__ = "procedure_version_history"

    version_id = Column(Integer, primary_key=True, index=True)
    procedure_id = Column(Integer, ForeignKey("cleaning_procedures.procedure_id"), nullable=False)
    version_number = Column(String, nullable=False)
    changed_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    change_summary = Column(String, nullable=True)
    archived_date = Column(Date, nullable=False)
    previous_version_id = Column(
        Integer,
        ForeignKey("procedure_version_history.version_id"),
        nullable=True,
    )

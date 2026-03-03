import enum

from sqlalchemy import Column, Integer, String, Date, Enum, ForeignKey

from app.database import Base


class FlagType(str, enum.Enum):
    unclear = "unclear"
    better_method = "better_method"
    caused_issue = "caused_issue"


class FlagStatus(str, enum.Enum):
    open = "open"
    reviewed = "reviewed"
    actioned = "actioned"


class InstructionFlag(Base):
    __tablename__ = "instruction_flags"

    flag_id = Column(Integer, primary_key=True, index=True)
    substep_id = Column(Integer, ForeignKey("substeps.substep_id"), nullable=False)
    reported_by = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    flag_type = Column(Enum(FlagType), nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(FlagStatus), nullable=False, default=FlagStatus.open)
    created_date = Column(Date, nullable=False)

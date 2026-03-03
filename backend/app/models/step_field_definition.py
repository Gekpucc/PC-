import enum

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, Enum, JSON

from app.database import Base


class FieldType(str, enum.Enum):
    text = "text"
    number = "number"
    checkbox_group = "checkbox_group"
    dropdown = "dropdown"
    table = "table"


class StepFieldDefinition(Base):
    __tablename__ = "step_field_definitions"

    step_field_id = Column(Integer, primary_key=True, index=True)
    step_id = Column(Integer, ForeignKey("steps.step_id"), nullable=False)
    field_type = Column(Enum(FieldType), nullable=False)
    field_label = Column(String, nullable=False)
    options = Column(JSON, nullable=True)
    required = Column(Boolean, nullable=False, default=False)
    min_value = Column(Float, nullable=True)
    max_value = Column(Float, nullable=True)
    spec_limit_low = Column(Float, nullable=True)
    spec_limit_high = Column(Float, nullable=True)
    table_columns = Column(JSON, nullable=True)

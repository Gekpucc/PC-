from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.sql import func

from app.database import Base


class TagTemplate(Base):
    __tablename__ = "tag_templates"

    tag_template_id = Column(Integer, primary_key=True, index=True)
    part_id = Column(Integer, ForeignKey("parts.part_id"), nullable=False)
    template_layout = Column(Text, nullable=True)
    fields_required = Column(Text, nullable=True)
    last_updated = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

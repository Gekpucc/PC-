from sqlalchemy import Column, Integer, String, ForeignKey
from app.database import Base


class Part(Base):
    __tablename__ = "parts"

    part_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey("customers.customer_id"), nullable=False)
    part_number = Column(String, nullable=False)
    description = Column(String, nullable=True)
    material = Column(String, nullable=True)
    spec = Column(String, nullable=True)

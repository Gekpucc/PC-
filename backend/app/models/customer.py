from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contact = Column(String, nullable=True)
    itar_flag = Column(Boolean, nullable=False, default=False)

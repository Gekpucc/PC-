import enum

from sqlalchemy import Column, Integer, String, Enum
from app.database import Base


class UserRole(str, enum.Enum):
    admin = "Admin"
    ops_manager = "Ops Manager"
    sales_manager = "Sales Manager"
    qa_internal = "QA Internal"
    quality_source = "Quality Source"
    technician = "Technician"
    shipping_receiving = "Shipping & Receiving"


class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)
    email = Column(String, nullable=True, unique=True)
    username = Column(String, nullable=True, unique=True, index=True)
    password_hash = Column(String, nullable=True)

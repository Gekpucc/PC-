from sqlalchemy import Column, Integer, String

from app.database import Base


class Bath(Base):
    __tablename__ = "baths"

    bath_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    type = Column(String, nullable=True)
    chemical = Column(String, nullable=True)
    current_status = Column(String, nullable=True)

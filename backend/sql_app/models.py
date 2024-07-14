from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class BatteryLocation(Base):
    __tablename__ = 'battery'
    number = Column(Integer,primary_key=True, nullable=True)
    administrative_dong = Column(String(50), nullable=True)
    location= Column(String(50), nullable=True)
    note = Column(String(50),nullable=True)
    data_reference_date = Column(String(50),nullable=True)
    # battery = relationship("Battery", back_populates="owner")

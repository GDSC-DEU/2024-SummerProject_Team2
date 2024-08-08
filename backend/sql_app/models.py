from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base


class BatteryLocation(Base):
    __tablename__ = 'battery'
    number = Column(Integer,primary_key=True, nullable=False)
    administrative_dong = Column(String(50), nullable=False)
    location= Column(String(50), nullable=False)
    note = Column(String(50),nullable=False)
    data_reference_date = Column(String(50),nullable=False)
    latitude = Column(Float(50),nullable=False)
    longitude = Column(Float(50),nullable=False)


class User(Base):
    __tablename__ = 'user'

    email = Column(String(50), unique=True, nullable=False, primary_key=True)
    user_name = Column(String(50), nullable=False)
    password = Column(String(300), nullable=False)
    region = Column(String(50),nullable=False)
    is_active = Column(Boolean,default=True)

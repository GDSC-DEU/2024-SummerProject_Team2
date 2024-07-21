from typing import List, Optional
from pydantic import BaseModel,EmailStr

class BatteryLocation(BaseModel):
    number: int
    administrative_dong: str
    location: str
    note: str
    data_reference_date: str
    class Config:
        orm_mode = True

class UserRegister(BaseModel):
    email: str
    password: str
    user_name: str

    class Config:
        orm_mode = True

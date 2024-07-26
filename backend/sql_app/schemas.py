from typing import List, Optional
from pydantic import BaseModel,EmailStr,validator
class BatteryLocation(BaseModel):
    number: int
    administrative_dong: str
    location: str
    note: str
    data_reference_date: str
    latitude: float
    longitude: float
    class Config:
        orm_mode = True

class BatteryCoordinates(BaseModel):
    latitude: float
    longitude: float
    class Config:
        orm_mode = True
        
class UserRegister(BaseModel):
    email: EmailStr
    password: str
    user_name: str
    region: str
    @validator('email','user_name','region','password')
    def check_empty(cls, v):
        if v == '':
            raise ValueError('항목을 모두 입력해주세요')
        return v
    @validator('password')
    def validate_password(cls, v):
        if len(v) < 8:
            raise ValueError('비밀번호는 8자 이상이어야 합니다')
        return v

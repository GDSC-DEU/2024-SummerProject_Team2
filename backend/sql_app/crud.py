from sqlalchemy.orm import Session
import jwt
from . import models, schemas
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import os
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def show_battery_location(db: Session, skip: int = 0):
    return db.query(models.BatteryLocation).offset(skip).all()

def show_battery_coordinates(db: Session, skip: int = 0):
    return db.query(models.BatteryLocation.latitude, models.BatteryLocation.longitude).offset(skip).all()

def password_auth(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_user(db: Session, user_email: str):
    print(models.User)
    return db.query(models.User).filter(models.User.email == user_email).first()

def create_user(user: schemas.UserRegister,db: Session):
    db_user = models.User(email=user.email, 
                          user_name=user.user_name, 
                          password=pwd_context.hash(user.password), 
                          region=user.region)
    db.add(db_user)
    db.commit()
    
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

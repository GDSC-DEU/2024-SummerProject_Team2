from sqlalchemy.orm import Session
import jwt
from . import models, schemas, crud,database
from fastapi import Depends, FastAPI, HTTPException, status
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone
import os
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from jose import JWTError, jwt
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def show_battery_location(db: Session, skip: int = 0):
    return db.query(models.BatteryLocation).offset(skip).all()

def show_battery_coordinates(db: Session, skip: int = 0):
    return db.query(models.BatteryLocation.latitude, models.BatteryLocation.longitude).offset(skip).all()

def password_auth(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_user_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def get_user(db:Session,user_name: str):
    return db.query(models.User).filter(models.User.user_name == user_name).first()

def authenticate_user(db: Session, user_name: str, password: str):
    hashed_password = get_password_hash(password)
    user = {get_user(db, user_name):hashed_password}
    if not user:
        return False
    if not password_auth(password, hashed_password):
        return False
    return hashed_password

def create_user(user: schemas.UserRegister,db: Session):
    db_user = models.User(email=user.email, 
                          user_name=user.user_name, 
                          password=pwd_context.hash(user.password), 
                          region=user.region,
                          is_active=True)
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

async def get_current_user(db: Session = Depends(database.get_db),token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(current_user: schemas.User = Depends(get_current_user)):
    if current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

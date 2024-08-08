from fastapi import APIRouter,Response,Request
from typing import Annotated
from sqlalchemy.orm import Session
from sql_app import schemas, crud, database, models
from fastapi import APIRouter, Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from sql_app import schemas, crud, database
import os
from dotenv import load_dotenv
from datetime import timedelta
from fastapi.responses import JSONResponse

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 60
router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
db = database.SessionLocal()
@router.post(path="/signup")
async def signup(new_user: schemas.UserRegister,db: Session = Depends(database.get_db)):
    user = crud.get_user_email(db,new_user.email)
    if user:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")
        # 올바른 세션 인스턴스를 사용하여 사용자 생성
    crud.create_user(new_user, db)

    return {"message": "회원가입 성공"}


@router.post(path="/signin")
async def signin(response: Response,login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_user_email(db,login_form.username)

    if not user:
        raise HTTPException(status_code=400, detail="유효하지 않은 사용자입니다.")
    
    res = crud.password_auth(login_form.password, user.password)

    acess_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    acess_token = crud.create_access_token(data={"sub": user.email}, expires_delta=acess_token_expires)

    response.set_cookie(key="access_token", value=acess_token, httponly=True)

    if not res:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    
    return schemas.Token(access_token=acess_token, token_type="bearer")

@router.post(path="/signout")
async def signout(response: Response,request: Request):
    response.delete_cookie(key="access_token")

    return HTTPException(status_code=200, detail="로그아웃 성공")

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = crud.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = crud.create_access_token(
        data={"sub": user.user_name}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("me/", response_model=schemas.User)
async def read_users_me(
    current_user: Annotated[schemas.User, Depends(crud.get_current_active_user)],
):
    return current_user


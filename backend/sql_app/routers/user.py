from sqlalchemy.orm import Session
from sql_app import schemas, crud, database
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
router = APIRouter()

@router.post(path="/signup")
async def signup(new_user: schemas.UserRegister,db: Session = Depends(database.get_db)):
    db = database.SessionLocal()
    user = crud.get_user(db, user_email=new_user.email)
    if user:
        raise HTTPException(status_code=400, detail="이미 존재하는 이메일입니다.")
        # 올바른 세션 인스턴스를 사용하여 사용자 생성
    crud.create_user(new_user, db)

    return {"message": "회원가입 성공"}

@router.post(path="/signin")
async def signin(login_form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = crud.get_user(db, user_email=login_form.username)

    if not user:
        raise HTTPException(status_code=400, detail="유효하지 않은 사용자입니다.")
    
    res = crud.password_auth(login_form.password, user.password)

    if not res:
        raise HTTPException(status_code=400, detail="비밀번호가 일치하지 않습니다.")
    
    return {"message": "로그인 성공"}

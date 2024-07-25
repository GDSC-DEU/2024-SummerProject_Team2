from sqlalchemy.orm import Session

from . import models, schemas
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def show_battery_location(db: Session, skip: int = 0):
    return db.query(models.BatteryLocation).offset(skip).all()
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
    
# def show_unsolved_problem(db: Session, skip: int = 0):
#     return db.query(models.UnsolvedProblem).offset(skip).all()
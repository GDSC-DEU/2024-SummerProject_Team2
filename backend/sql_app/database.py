from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:1234@113.198.230.24:318/summer"
#"mysql+pymysql://root:@localhost:3306/gdsc"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    print(os.getenv("SQLALCHEMY_DATABASE_URL"))
    try:
        yield db
    finally:
        db.close()

def init_db():
    # 여기에서 모델을 임포트하여 Base.metadata.create_all이 모든 테이블을 인식하도록 합니다.
    from . import models
    Base.metadata.create_all(bind=engine)
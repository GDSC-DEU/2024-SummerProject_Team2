from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List
from sql_app.routers import admin, user
from sql_app.middlewares import add_middlewares
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/users", tags=["users"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "분리배출 합시다 !"}


@app.get("/battery", response_model=List[schemas.BatteryLocation])
def show_battery_location(skip: int = 0, db: Session = Depends(get_db)):
    battery = crud.show_battery_location(db, skip=skip)
    if not battery:
        raise HTTPException(status_code=404, detail="Battery Location not found")
    return battery

# @app.get("/unsolved",response_model=List[schemas.UnsovledProblem])
# def show_unsolved(skip: int = 0, db: Session = Depends(get_db)):
#     unsolved = crud.show_unsolved_problem(db, skip=skip)
#     if not unsolved:
#         raise HTTPException(status_code=404, detail="All problems not found")
#     return unsolved



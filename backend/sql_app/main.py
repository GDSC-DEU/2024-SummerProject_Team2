from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from typing import List
from sql_app.routers import admin, user, example_router
from sql_app.middlewares import add_middlewares
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

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

templates = Jinja2Templates(directory="sql_app/template")
app.mount("/static", StaticFiles(directory="sql_app/static"), name="static")

app.include_router(admin.router, prefix="/admin", tags=["admin"])
app.include_router(user.router, prefix="/users", tags=["users"])
app.include_router(example_router.router)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/battery", response_model=List[schemas.BatteryLocation])
def show_battery_location(skip: int = 0, db: Session = Depends(get_db)):
    battery = crud.show_battery_location(db, skip=skip)
    if not battery:
        raise HTTPException(status_code=404, detail="Battery Location not found")
    return battery




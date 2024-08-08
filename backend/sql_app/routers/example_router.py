from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

templates = Jinja2Templates(directory="sql_app/template")

@router.get("/", response_class=HTMLResponse)
async def read_main(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@router.get("/sign_in", response_class=HTMLResponse)
async def read_sign_in(request: Request):

    return templates.TemplateResponse("sign_in.html", {"request": request})

@router.get("/sign_up", response_class=HTMLResponse)
async def read_sign_up(request: Request):
    return templates.TemplateResponse("sign_up.html", {"request": request})

@router.get("/near", response_class=HTMLResponse)
async def read_sign_in(request: Request):
    naver_api_key = os.getenv("NAVER_MAP_API_KEY") 
    return templates.TemplateResponse("near.html", {"request": request, "NAVER_API_KEY": naver_api_key})

@router.get("/oversize_waste", response_class=HTMLResponse)
async def read_sign_in(request: Request):
    return templates.TemplateResponse("oversize_waste.html", {"request": request})

@router.get("/search", response_class=HTMLResponse)
async def read_sign_in(request: Request):
    return templates.TemplateResponse("search.html", {"request": request})


from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

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
    return templates.TemplateResponse("near.html", {"request": request})

@router.get("/oversize_waste", response_class=HTMLResponse)
async def read_sign_in(request: Request):
    return templates.TemplateResponse("oversize_waste.html", {"request": request})

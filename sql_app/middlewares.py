from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.cors import CORSMiddleware

class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # 요청 전 처리 로직
        response = await call_next(request)
        # 응답 후 처리 로직
        return response

def add_middlewares(app: FastAPI):
    app.add_middleware(CustomMiddleware)

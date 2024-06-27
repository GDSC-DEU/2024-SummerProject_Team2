from fastapi import APIRouter, Depends
from sql_app import schemas, crud, database

router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_data():
    # 대시보드 데이터를 반환하는 로직
    return {"message": "Admin Dashboard Data"}

# 다른 관리자 관련 라우터들 추가

from fastapi import APIRouter, Depends
from sql_app import schemas, crud, database
import psutil
router = APIRouter()

@router.get("/dashboard")
async def get_dashboard_data():
    # 대시보드 데이터를 반환하는 로직
    return {"message": "Admin Dashboard Data"}

# 다른 관리자 관련 라우터들 추가
@router.get("/status")
def get_status():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    
    status = {
        "cpu_usage": cpu_usage,
        "memory": {
            "total": memory_info.total,
            "available": memory_info.available,
            "percent": memory_info.percent,
            "used": memory_info.used,
            "free": memory_info.free
        },
        "disk": {
            "total": disk_usage.total,
            "used": disk_usage.used,
            "free": disk_usage.free,
            "percent": disk_usage.percent
        }
    }
    
    return status

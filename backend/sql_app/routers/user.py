from fastapi import APIRouter

router = APIRouter()

@router.get("/profile")
async def get_user_profile():
    return {"message": "User Profile Data"}

# 다른 사용자 관련 라우터들 추가

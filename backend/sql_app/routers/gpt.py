from fastapi import FastAPI, HTTPException,APIRouter,Response,Request
from pydantic import BaseModel
from dotenv import load_dotenv
from sql_app import schemas
import os
from openai import OpenAI
import openai 
import json

router = APIRouter()
load_dotenv()
# API 키를 사용하여 OpenAI API 설정
@router.post(path="/gpt")
async def get_gpt_response(request: schemas.GPTRequest):
    client = OpenAI(
    api_key = os.getenv("OPEN_API_KEY")
    )
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "\"품목\":품목이름,\"재활용여부\":가능/불가능,\"재활용방법\":4단계로(앞에 숫자없이) 이 양식은 무조건 맞춰서 대답해줘"},
                {"role": "user", "content": f"json형식으로 {request} 분리수거 하는법"}
            ],
            response_format = {"type": "json_object"}
        )
        result = response.choices[0].message.content
        return json.loads(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

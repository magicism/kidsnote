from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from app.chatbot import get_response
import os
import openai

app = FastAPI()

# CORS 설정 추가 (웹 UI에서 API 호출 가능하도록 허용)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인 허용 (보안 필요하면 특정 도메인만 허용)
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메서드 허용
    allow_headers=["*"],  # 모든 헤더 허용
)

# OpenAI API 키 설정
openai.api_key = os.getenv("OPENAI_API_KEY")

class ChatRequest(BaseModel):
    input_text: str

@app.get("/")
def home():
    return {"message": "키즈노트 챗봇 API"}

@app.post("/chat")
async def chat(request: ChatRequest):
    try:
        response = get_response(request.input_text)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"서버 오류: {str(e)}")

# 📌 `GET` 요청도 지원하도록 추가
@app.get("/chat")
async def chat_get(input_text: str):
    return await chat(ChatRequest(input_text=input_text))
